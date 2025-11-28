PYTHON = python3

clean:
	rm -rf data/*

ingest:
	$(PYTHON) src/cobit/ingestion/ingestion_pipeline.py

main:
	$(PYTHON) -m cobit.main
