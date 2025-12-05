from cobit.kraken.kraken_client import make_request
from cobit.utils.config import ENDPOINTS

def system_status():
    """Retrieve the current system status."""
    return make_request(ENDPOINTS['system_status'])

def server_time():
    """Retrieve the current server time."""
    return make_request(ENDPOINTS['server_time'])

def order_book(pair: str, count: int):
    """Retrieve the live order book for a given currency pair."""
    query = {
        'pair': pair,
        'count': count,
    }

    return make_request(path=ENDPOINTS['order_book'], query=query)

def market_trades(pair: str, count: int):
    """Retrieve the most recent trades for a given currency pair."""
    query = {
        'pair': pair,
        'count': count,
    }

    return make_request(path=ENDPOINTS['market_trades'], query=query)
