from cobit.ingestion.ingestion_pipeline import ingest_market_trades, ingest_order_book
from cobit.storage.store_parquets import save_table_to_parquet
from cobit.utils.config import CONFIG, PATHS

if __name__ == '__main__':
    ingested_market_trades = ingest_market_trades(CONFIG['currency_pairs']['BTC_USD'], 1000)
    print(f'--------------------------')
    print(f'| ingested_market_trades |')
    print(f'--------------------------')
    print(f'{ingested_market_trades}')
    save_table_to_parquet(
        table=ingested_market_trades,
        directory=PATHS['dirs']['market_trades_parquets'],
        filename=PATHS['files']['market_trades_parquet'],
    )

    ingested_order_book = ingest_order_book(CONFIG['currency_pairs']['BTC_USD'], 10)
    print(f'-----------------------')
    print(f'| ingested_order_book |')
    print(f'-----------------------')
    print(f'{ingested_order_book}')
    save_table_to_parquet(
        table=ingested_order_book,
        directory=PATHS['dirs']['order_book_parquets'],
        filename=PATHS['files']['order_book_parquet'],
    )
