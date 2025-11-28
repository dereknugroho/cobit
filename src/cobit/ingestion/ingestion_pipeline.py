from cobit.ingestion.market_trades_ingestion import generate_market_trades_table
from cobit.ingestion.order_book_ingestion import generate_order_book_table
from cobit.kraken.exceptions import KrakenAPIError
from cobit.kraken.kraken_services import market_trades, order_book
from cobit.utils.config import CONFIG, FILEPATHS
from cobit.utils.io import save_raw_api_response_json

def ingest_market_trades(pair: str = 'BTC/USD', count: int = 1000):
    """Fetch Kraken trades for a currency pair and convert them into a PyArrow table."""
    # Retrieve market trading data from the Kraken API
    response = market_trades(pair, count)

    # Handle Kraken error format
    if response.get('error'):
        raise KrakenAPIError(response['error'])
    
    # Save raw Kraken API response in JSON
    save_raw_api_response_json(
        response=response,
        directory=FILEPATHS['dir_raw_kraken_api_response_market_trades'],
        filename=FILEPATHS['market_trades_raw'],
    )

    # Convert raw trade data into a PyArrow table
    raw_trades = response['result'][pair]
    table = generate_market_trades_table(raw_trades)

    return table

def ingest_order_book(pair: str = 'BTC/USD', count: int = 100):
    """Fetch Kraken order book for a currency pair and convert into a PyArrow table."""
    # Retrieve order book data from the Kraken API
    response = order_book(pair, count)

    # Handle Kraken error format
    if response.get('error'):
        raise KrakenAPIError(response['error'])

    # Save raw Kraken API response in JSON
    save_raw_api_response_json(
        response=response,
        directory=FILEPATHS['dir_raw_kraken_api_response_order_book'],
        filename=FILEPATHS['order_book_raw'],
    )

    # Convert raw order book data into a PyArrow table
    raw_order_book = response['result'][pair]
    table = generate_order_book_table(raw_order_book)

    return table

if __name__ == '__main__':
    ingested_market_trades = ingest_market_trades(CONFIG['currency_pairs']['BTC_USD'], 1000)
    print(f'--------------------------')
    print(f'| ingested_market_trades |')
    print(f'--------------------------')
    print(f'{ingested_market_trades}')

    ingested_order_book = ingest_order_book(CONFIG['currency_pairs']['BTC_USD'], 10)
    print(f'-----------------------')
    print(f'| ingested_order_book |')
    print(f'-----------------------')
    print(f'{ingested_order_book}')
