import json
import pandas as pd
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
CLEAN_DIR = ROOT / "data" / "clean"

WANT = ["USD", "EUR", "RSD", "CNY", "GBP", "CHF", "KZT"]


def transform():
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    latest = sorted(RAW_DIR.glob("cbr_*.json"))[-1]
    print("читаю", latest)

    with open(latest, encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for code in WANT:
        if code not in data["Valute"]:
            continue
        v = data["Valute"][code]
        rows.append({
            "code": code,
            "name": v["Name"],
            "value": v["Value"],
            "previous": v["Previous"],
        })

    df = pd.DataFrame(rows)
    df["value"] = df["value"].astype(float)
    df["previous"] = df["previous"].astype(float)
    df["diff"] = df["value"] - df["previous"]
    df["diff_pct"] = (df["diff"] / df["previous"] * 100).round(2)
    df["date"] = pd.to_datetime(data["Date"]).date()
    df = df[["date", "code", "name", "value", "previous", "diff", "diff_pct"]]

    print(df)

    out = CLEAN_DIR / f"rates_{datetime.now().strftime('%Y-%m-%d')}.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print("сохранил", out)


if __name__ == "__main__":
    transform()