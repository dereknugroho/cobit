import pyarrow as pa

from cobit.utils.config import NUM_FIELDS

# -----------------------------------------------------------------------------
# SCHEMA (declared once for module-wide reuse)
# -----------------------------------------------------------------------------

MARKET_TRADES_SCHEMA = pa.schema([
    ('trade_id', pa.int64()),
    ('price', pa.float64()),
    ('quantity', pa.float64()),
    ('timestamp', pa.timestamp('s')),
    ('side', pa.dictionary(pa.int8(), pa.string())),
    ('order_type', pa.dictionary(pa.int8(), pa.string())),
])

# -----------------------------------------------------------------------------
# TABLE GENERATOR
# -----------------------------------------------------------------------------

def generate_market_trades_table(
    market_trades: list[list[object]],
    schema: pa.Schema = MARKET_TRADES_SCHEMA,
) -> pa.Table:
    """
    Convert Kraken trade data into a strongly-typed PyArrow table.

    Parameters
    ----------
    market_trades : list of list
        Raw trades from Kraken's API in the format:
        [price, quantity, timestamp, side, order_type, misc, trade_id]

    schema : pa.Schema
        Arrow schema to enforce for the generated table.

    Returns
    -------
    pa.Table
        Strongly-typed Arrow table of market trades.

    Raises
    ------
    ValueError
        If input data is malformed or contains unexpected shapes.
    """

    # -----------------------
    # 1. Validate input
    # -----------------------
    if not market_trades:
        # Return an empty table with the correct schema
        return pa.Table.from_batches([], schema=schema)

    for i, trade in enumerate(market_trades):
        if len(trade) != NUM_FIELDS['market_trades']:
            raise ValueError(
                f"Trade at index {i} has {len(trade)} elements, expected {NUM_FIELDS['market_trades']}. Trade: {trade}"
            )

    # -----------------------
    # 2. Column extraction
    # -----------------------
    # Transpose list-of-lists into columns
    prices, quantities, timestamps, sides, order_types, _misc, trade_ids = zip(*market_trades)

    # -----------------------
    # 3. Build Arrow arrays
    # -----------------------
    arrays = [
        pa.array([int(tid) for tid in trade_ids], type=pa.int64()),
        pa.array([float(p) for p in prices], type=pa.float64()),
        pa.array([float(q) for q in quantities], type=pa.float64()),
        pa.array([int(ts) for ts in timestamps], type=pa.timestamp('s')),
        pa.array(sides, type=pa.string()).dictionary_encode(),
        pa.array(order_types, type=pa.string()).dictionary_encode(),
    ]

    batch = pa.record_batch(arrays, schema=schema)

    return pa.Table.from_batches([batch])
