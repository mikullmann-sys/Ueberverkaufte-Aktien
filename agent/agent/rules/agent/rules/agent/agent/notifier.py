import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def notify(results):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("Telegram credentials missing")

    if not results:
        message = "📉 Market Agent – Überverkaufte Aktien\n\nKeine Treffer heute."
    else:
        lines = ["📉 Market Agent – Überverkaufte Aktien\n"]
        for r in results:
            lines.append(f"• {r['ticker']} (Score: {r['score']})")
            for rule, score in r["rules"]:
                lines.append(f"   - {rule} (+{score})")
            lines.append("")
        message = "\n".join(lines)

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)
