from agent.data_loader import load_sp500_tickers, load_price_data
from agent.config import RED_STREAK_DAYS, RSI_THRESHOLD
from agent.rules.red_streak import red_streak
from agent.rules.rsi import rsi_oversold

RULES = {
    "6 red days": {
        "func": lambda df: red_streak(df, RED_STREAK_DAYS),
        "score": 2
    },
    "RSI oversold": {
        "func": lambda df: rsi_oversold(df, RSI_THRESHOLD),
        "score": 1
    }
}

MIN_RULES = 2

def run_agent():
    results = []
    tickers = load_sp500_tickers()

    for ticker in tickers:
        try:
            df = load_price_data(ticker)
            if df.empty:
                continue

            matched = []
            score = 0

            for name, rule in RULES.items():
                if rule["func"](df):
                    matched.append((name, rule["score"]))
                    score += rule["score"]

            if len(matched) >= MIN_RULES:
                results.append({
                    "ticker": ticker,
                    "score": score,
                    "rules": matched
                })

        except Exception:
            continue

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
