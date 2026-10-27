import os
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Загружаем настройки
load_dotenv()
DB_URL = os.getenv("DB_URL")

# Настройка страницы
st.set_page_config(page_title="Курсы валют ЦБ", layout="wide")
st.title("📊 Дашборд курсов валют ЦБ РФ")

# Подключаемся к базе и забираем данные
engine = create_engine(DB_URL)
df = pd.read_sql("SELECT * FROM rates ORDER BY date DESC", engine)

if df.empty:
    st.warning("В базе пока нет данных. Запусти main.py!")
else:
    # Боковая панель с фильтрами
    st.sidebar.header("Фильтры")

    # Выбор валют
    currencies = df["code"].unique().tolist()
    selected_cur = st.sidebar.multiselect("Выбери валюты:", currencies, default=["USD", "EUR"])

    # Фильтруем данные
    filtered_df = df[df["code"].isin(selected_cur)]

    # Разделяем экран на две колонки
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Текущие курсы")
        # Выводим таблицу только с нужными колонками
        st.dataframe(filtered_df[["date", "code", "name", "value", "diff_pct"]])

    with col2:
        st.subheader("Изменение курса за день (%)")
        # Строим график
        fig = px.bar(
            filtered_df,
            x="code",
            y="diff_pct",
            color="diff_pct",
            color_continuous_scale=["red", "gray", "green"],
            labels={"code": "Валюта", "diff_pct": "Изменение (%)"},
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)