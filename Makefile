PYTHON = python3

all: clean ingest storage

clean: clean-data clean-logs

clean-data:
	rm -rf data/

clean-logs:
	rm -rf logs/

ingest:
	$(PYTHON) src/cobit/ingestion/ingestion_pipeline.py

storage:
	$(PYTHON) src/cobit/storage/storage_pipeline.py

main:
	$(PYTHON) -m cobit.main
