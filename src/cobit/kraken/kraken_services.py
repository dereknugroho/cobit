from cobit.kraken.kraken_client import make_request
from cobit.utils.config import CONFIG, ENDPOINTS

def system_status():
    """Retrieve the current system status."""
    return make_request(ENDPOINTS['system_status'])

def server_time():
    """Retrieve the current server time."""
    return make_request(ENDPOINTS['server_time'])

def order_book(pair: str = "BTC/USD"):
    """Retrieve the live order book for a given currency pair."""
    query = {'pair': pair}

    return make_request(path=ENDPOINTS['order_book'], query=query)

def recent_market_trades(pair: str = "BTC/USD", count: int = 1000):
    """Retrieve the most recent trades for a given currency pair."""
    query = {
        'pair': pair,
        'count': count,
    }

    return make_request(path=ENDPOINTS['recent_market_trades'], query=query)

def recent_market_spreads(pair: str = CONFIG['currency_pairs']['BTC_USD']):
    """Retrieve the live order book for a given currency pair."""
    query = {'pair': pair}

    return make_request(path=ENDPOINTS['recent_market_spreads'], query=query)
