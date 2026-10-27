CREATE TABLE IF NOT EXISTS rates (
    id          SERIAL PRIMARY KEY,
    date        DATE           NOT NULL,
    code        VARCHAR(3)     NOT NULL,
    name        VARCHAR(100)   NOT NULL,
    value       NUMERIC(12, 4) NOT NULL,
    previous    NUMERIC(12, 4) NOT NULL,
    diff        NUMERIC(12, 4) NOT NULL,
    diff_pct    NUMERIC(8, 2)  NOT NULL,
    created_at  TIMESTAMP      DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_rates_code_date ON rates (code, date);