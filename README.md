# Data Engineering Projects

Data engineering projects with Python, SQL, Pandas, and ETL workflows for data pipelines, validation, and data quality.

Built by Richard Frimpong.

## What is in here

- `etl_example.py` — a small ETL example. It reads `sample_data.csv`, cleans it, validates it, and writes `cleaned_data.csv`.
- `sample_data.csv` — a tiny sample dataset to run it with.
- `schema.sql` — the table the cleaned data would load into.

These are example / learning scripts, not a production pipeline.

## Try it

```bash
python3 etl_example.py
```

## Steps in the example

1. Extract — read the CSV.
2. Transform — drop rows with missing values, normalise text, parse dates.
3. Validate — check for duplicate IDs and out-of-range values, and report them.
4. Load — write the cleaned CSV, ready for the table in `schema.sql`.
