from ta.momentum import RSIIndicator

def rsi_oversold(df, threshold):
    if len(df) < 14:
        return False
    rsi = RSIIndicator(df["Close"]).rsi()
    return rsi.iloc[-1] < threshold
