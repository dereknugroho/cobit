import pyarrow as pa

from cobit.utils.config import CONFIG, NUM_FIELDS

ORDER_BOOK_SCHEMA = pa.schema([
    ('index', pa.int64()),
    ('price', pa.float64()),
    ('quantity', pa.float64()),
    ('timestamp', pa.timestamp('s')),
    ('side', pa.dictionary(pa.int8(), pa.string()))
])

def generate_order_book_table(
    order_book: dict[str, list[list[object]]],
    schema: pa.Schema = ORDER_BOOK_SCHEMA
) -> pa.Table:
    """
    Convert Kraken order book into a strongly-typed PyArrow table.

    Parameters
    ----------
    order_book : dict [str: list of list]
        Raw order book from Kraken's API in the format:
        side: [price, quantity, time]

    schema : pa.Schema
        Arrow schema to enforce for the generated table.

    Returns
    -------
    pa.Table
        Strongly-typed Arrow table of the order book.

    Raises
    ------
    ValueError
        If input data is malformed or contains unexpected shapes.
    """

    # Validate input
    if not order_book:
        return pa.Table.from_batches([], schema=schema)

    for side in CONFIG['sides']:
        for i, order in enumerate(order_book[side]):
            if len(order) != NUM_FIELDS['order_book']:
                raise ValueError(
                    f"Order at index {i} has {len(order)} elements, expected {NUM_FIELDS['order_book']}. Order: {order}"
                )

    # Extract columns
    rows = []

    # Append side to each order
    for side in CONFIG['sides']:
        for price, quantity, ts in order_book.get(side, []):
            rows.append([price, quantity, ts, side[:-1]])

    # Transpose list-of-lists into columns
    prices, quantities, timestamps, sides = zip(*rows)

    # Construct arrays
    arrays = [
        pa.array([int(i) for i in range(len(rows))], type=pa.int64()),
        pa.array([float(p) for p in prices], type=pa.float64()),
        pa.array([float(q) for q in quantities], type=pa.float64()),
        pa.array([float(ts) for ts in timestamps], type=pa.timestamp('s')),
        pa.array(sides, type=pa.string()).dictionary_encode()
    ]

    # Generate table
    table = pa.Table.from_batches([pa.record_batch(arrays, schema=schema)])

    return table
