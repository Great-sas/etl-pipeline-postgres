import requests
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def extract():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    data = requests.get(URL, timeout=10).json()

    today = datetime.now().strftime("%Y-%m-%d")
    out = RAW_DIR / f"cbr_{today}.json"

    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("сохранил", out)


if __name__ == "__main__":
    extract()