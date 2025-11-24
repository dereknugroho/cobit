PYTHON = python3

ingest:
	$(PYTHON) src/cobit/ingestion/market_trades_ingestion.py

main:
	$(PYTHON) -m cobit.main
