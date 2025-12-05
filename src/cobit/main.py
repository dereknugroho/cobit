from cobit.ingestion.ingestion_pipeline import ingest_market_trades, ingest_order_book

if __name__ == '__main__':
    ingest_market_trades()
    ingest_order_book()
