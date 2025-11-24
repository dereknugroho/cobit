PYTHON = python3

ingest:
	$(PYTHON) src/cobit/ingestion/ingestion_pipeline.py

main:
	$(PYTHON) -m cobit.main
