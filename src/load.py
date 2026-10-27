import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
CLEAN_DIR = ROOT / "data" / "clean"
SQL_DIR = ROOT / "sql"

# Загружаем пароль из .env
load_dotenv(ROOT / ".env")
DB_URL = os.getenv("DB_URL")


def load():
    engine = create_engine(DB_URL)
    print("подключился к Postgres")

    # Читаем SQL-файл и создаем таблицу
    schema = (SQL_DIR / "schema.sql").read_text(encoding="utf-8")
    with engine.begin() as conn:
        conn.execute(text(schema))
    print("схема применена")

    # Берем самый свежий CSV
    latest = sorted(CLEAN_DIR.glob("rates_*.csv"))[-1]
    print("читаю", latest)
    df = pd.read_csv(latest, parse_dates=['date'])

    # Заливаем в базу
    df.to_sql("rates", engine, if_exists="append", index=False)
    print(f"залил {len(df)} строк")

    # Проверяем
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM rates")).scalar()
    print("всего строк в таблице:", count)


if __name__ == "__main__":
    load()