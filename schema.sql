CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    value REAL NOT NULL CHECK (value >= 0 AND value <= 1000),
    date DATE NOT NULL
);