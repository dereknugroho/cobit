# COBIT — Cryptocurrency Order Book Ingestion Tool

COBIT is a production-grade data ingestion system that retrieves real-time
order book data from the Kraken cryptocurrency exchange and stores it locally
in a clean, analytics-ready format. It is designed as a standalone utility or
as the data ingestion component of larger ML pipelines.

## Usage

### 1. Create a Kraken account
Create a Kraken account [here](https://www.kraken.com/sign-up).

### 2. Obtain a Kraken API key
Obtain a Kraken API key [here](https://support.kraken.com/articles/360000919966-how-to-create-an-api-key).

### 3. Set Kraken API keys as environment variables
```
echo 'export API_KEY_KRAKEN="<Your Kraken public API key>"' >> ~/.zshrc
echo 'export API_SEC_KRAKEN="<Your Kraken secret API key>"' >> ~/.zshrc
source ~/.zshrc
```

### 4. Clone this repository
```
git clone git@github.com:dereknugroho/cobit.git
cd cobit
```

### 5. Run ingestion process
Execute `make all`:
```
make all
```

`make ingest` will retrieve data and can be executed as often as needed.

`make clean-data` will erase all data stored in `root/data/`.

`make clean-logs` will erase all logs stored in `root/logs/`.

`make clean` will execute `make clean-data` and `make clean-logs`.

### 6. All done!
Order book and market trading data is now available at `root/data/raw/kraken_api_response/`.
