PYTHON = python3

all: clean ingest

clean: clean-data clean-logs

clean-data:
	rm -rf data/

clean-logs:
	rm -rf logs/

ingest:
	$(PYTHON) src/cobit/ingestion/ingestion_pipeline.py
