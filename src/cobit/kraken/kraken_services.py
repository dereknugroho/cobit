from cobit.kraken.kraken_client import make_request
from cobit.utils.config import config

def system_status():
    """Retrieve the current system status."""
    return make_request(config['endpoints']['system_status'])

def server_time():
    """Retrieve the current server time."""
    return make_request(config['endpoints']['server_time'])

def order_book(pair: str = config['currency_pairs']['BTC_USD']):
    """Retrieve the live order book for a given currency pair."""
    query = {'pair': pair}

    return make_request(path=config['endpoints']['order_book'], query=query)

def recent_trades(pair: str = config['currency_pairs']['BTC_USD'], count: int = 1000):
    """Retrieve the most recent trades for a given currency pair."""
    query = {
        'pair': pair,
        'count': count,
    }

    return make_request(path=config['endpoints']['recent_trades'], query=query)

def recent_spreads(pair: str = config['currency_pairs']['BTC_USD']):
    """Retrieve the live order book for a given currency pair."""
    query = {'pair': pair}

    return make_request(path=config['endpoints']['recent_spreads'], query=query)
