import pandas as pd
import pyarrow as pa

def generate_empty_market_trades_df() -> pd.DataFrame:
    """
    Generate an empty dataframe on market trading activity.

    Columns:
    - trade_id
    - price
    - quantity
    - timestamp
    - side
    - order_type
    """
    schema = {
        "trade_id": pd.ArrowDtype(pa.int64()),
        "price": pd.ArrowDtype(pa.float64()),
        "quantity": pd.ArrowDtype(pa.float64()),
        "timestamp": pd.ArrowDtype(pa.timestamp('ns')),
        "side": pd.ArrowDtype(pa.string()),
        "order_type": pd.ArrowDtype(pa.string()),
    }

    df = pd.DataFrame({col: pd.Series(dtype=dt) for col, dt in schema.items()})
    return df

if __name__ == '__main__':
    market_trades = generate_empty_market_trades_df()
    print(f'{market_trades}')
