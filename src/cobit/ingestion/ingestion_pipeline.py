from cobit.ingestion.raw_exports import save_raw_api_response_json
from cobit.ingestion.market_trades_ingestion import generate_market_trades_table
from cobit.ingestion.order_book_ingestion import generate_order_book_table
from cobit.kraken.exceptions import KrakenAPIError
from cobit.kraken.kraken_services import market_trades, order_book
from cobit.utils.config import CONFIG, PATHS
from cobit.utils.logger import logger_setup, INFO

logger = logger_setup(
    __name__,
    CONFIG['logging']['ingestion_log'],
    INFO
)

def ingest_market_trades(pair: str = 'BTC/USD', count: int = 1000):
    """Fetch Kraken trades for a currency pair and convert them into a PyArrow table."""
    # Retrieve market trading data from the Kraken API
    response = market_trades(pair, count)

    # Save raw Kraken API response in JSON
    save_raw_api_response_json(
        response=response,
        directory=PATHS['dirs']['raw_kraken_api_response_market_trades'],
        filename=PATHS['files']['raw_market_trades'],
    )

    # Convert raw trade data into a PyArrow table
    raw_trades = response['result'][pair]
    table = generate_market_trades_table(raw_trades)

    logger.info(f'Successfully generated market_trades table')

    return table

def ingest_order_book(pair: str = 'BTC/USD', count: int = 100):
    """Fetch Kraken order book for a currency pair and convert into a PyArrow table."""
    # Retrieve order book data from the Kraken API
    response = order_book(pair, count)

    # Save raw Kraken API response in JSON
    save_raw_api_response_json(
        response=response,
        directory=PATHS['dirs']['raw_kraken_api_response_order_book'],
        filename=PATHS['files']['raw_order_book'],
    )

    # Convert raw order book data into a PyArrow table
    raw_order_book = response['result'][pair]
    table = generate_order_book_table(raw_order_book)

    logger.info(f'Successfully generated order_book table')

    return table

if __name__ == '__main__':
    ingested_market_trades = ingest_market_trades(CONFIG['currency_pairs']['BTC_USD'], 1000)
    ingested_order_book = ingest_order_book(CONFIG['currency_pairs']['BTC_USD'], 10)
