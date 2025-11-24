from cobit.ingestion.market_trades_ingestion import generate_market_trades_table
from cobit.kraken.kraken_services import recent_market_trades
from cobit.utils.config import CONFIG

def ingest_market_trades(pair: str):
    """Fetch Kraken trades for a pair and convert them into a PyArrow table."""
    response = recent_market_trades(pair=pair)

    # Handle Kraken error format
    if response.get('error'):
        raise ValueError(f'Kraken API error: {response["error"]}')

    raw_trades = response['result'][pair]
    table = generate_market_trades_table(raw_trades)

    return table

if __name__ == '__main__':
    ingested_market_trades = ingest_market_trades(CONFIG['currency_pairs']['BTC_USD'])
    print(f'--------------------------')
    print(f'| ingested_market_trades |')
    print(f'--------------------------')
    print(f'{type(ingested_market_trades)}')
    print(f'{ingested_market_trades}')
