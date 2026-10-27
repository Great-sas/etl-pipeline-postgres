# ETL Pipeline: CBR Currency Rates -> PostgreSQL -> Streamlit Dashboard

Pet project demonstrating Data Engineering and Analytics skills.

# Project Overview
An automated ETL pipeline that extracts data from the Central Bank of Russia's public API, cleans and transforms it using Pandas, and loads it into a PostgreSQL database. The final data is visualized using an interactive Streamlit dashboard.

Business value: Provides automated tracking of currency dynamics, eliminating the need for manual data collection in Excel.

# Tech Stack
- Python (Pandas, Requests, SQLAlchemy)
- PostgreSQL
- Docker
- Streamlit
- Git

# Architecture
The project follows the classic ETL layered approach:
1. Extract (`src/extract.py`): Downloads raw JSON data from the CBR API.
2. Transform (`src/transform.py`): Cleans data, enforces data types, and calculates daily rate changes.
3. Load (`src/load.py`): Creates the schema (`sql/schema.sql`) and loads clean data into PostgreSQL.
4. Dashboard (`dashboard.py`): Visualizes data from the database.

# How to Run
1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   Start PostgreSQL in Docker:

2. docker run --name etl-postgres -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=etl -p 5432:5432 -d postgres:16

3. Create a .env file in the root directory and add:
DB_URL=postgresql://postgres:secret@localhost:5432/etl

4.Run the ETL process:

python main.py

5.Launch the dashboard:
streamlit run dashboard.py



Results:

<img width="1911" height="974" alt="image" src="https://github.com/user-attachments/assets/9ea00ce9-0a22-4bea-bce4-674f1e7bc251" />
