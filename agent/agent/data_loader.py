import pandas as pd
import yfinance as yf
from agent.config import LOOKBACK_DAYS

def load_sp500_tickers():
    return pd.read_csv(
        "https://datahub.io/core/s-and-p-500-companies/r/constituents_symbols.txt",
        header=None
    )[0].tolist()

def load_price_data(ticker):
    return yf.download(
        ticker,
        period=f"{LOOKBACK_DAYS}d",
        interval="1d",
        progress=False
    )
