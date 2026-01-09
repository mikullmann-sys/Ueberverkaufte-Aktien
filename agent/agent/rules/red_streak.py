def red_streak(df, days):
    returns = df["Close"].pct_change()
    if len(returns) < days:
        return False
    return (returns.tail(days) < 0).all()
