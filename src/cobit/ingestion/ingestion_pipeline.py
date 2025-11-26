from cobit.ingestion.market_trades_ingestion import generate_market_trades_table
from cobit.ingestion.order_book_ingestion import generate_order_book_table
from cobit.kraken.exceptions import KrakenAPIError
from cobit.kraken.kraken_services import market_trades, order_book
from cobit.utils.config import CONFIG

def ingest_market_trades(pair: str = 'BTC/USD', count: int = 1000):
    """Fetch Kraken trades for a currency pair and convert them into a PyArrow table."""
    response = market_trades(pair, count)

    # Handle Kraken error format
    if response.get('error'):
        raise KrakenAPIError(response['error'])

    raw_trades = response['result'][pair]
    table = generate_market_trades_table(raw_trades)

    return table

def ingest_order_book(pair: str = 'BTC/USD', count: int = 100):
    """Fetch Kraken order book for a currency pair and convert into a PyArrow table."""
    response = order_book(pair, count)

    # Handle Kraken error format
    if response.get('error'):
        raise KrakenAPIError(response['error'])

    raw_order_book = response['result'][pair]
    table = generate_order_book_table(raw_order_book)

    return table

if __name__ == '__main__':
    ingested_market_trades = ingest_market_trades(CONFIG['currency_pairs']['BTC_USD'], 100)
    print(f'--------------------------')
    print(f'| ingested_market_trades |')
    print(f'--------------------------')
    print(f'{type(ingested_market_trades)}')
    print(f'{ingested_market_trades}')

    ingested_order_book = ingest_order_book(CONFIG['currency_pairs']['BTC_USD'], 10)
    print(f'-----------------------')
    print(f'| ingested_order_book |')
    print(f'-----------------------')
    print(f'{type(ingested_order_book)}')
    print(f'{ingested_order_book}')
