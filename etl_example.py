"""Example ETL pipeline with Python and Pandas.

Usage:
    python3 etl_example.py

Reads sample_data.csv, cleans and validates it, and writes
cleaned_data.csv. This is an example / learning script.
"""

import pandas as pd


def main():
    df = pd.read_csv("sample_data.csv")
    print(f"Extracted {len(df)} rows")

    # Transform: drop rows with missing values first, then normalise text
    # and parse dates.
    df = df.dropna(subset=["id", "name", "value", "date"])
    df["name"] = df["name"].astype(str).str.strip().str.title()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    # Validate: report duplicates and out-of-range values, then drop them.
    dupes = int(df.duplicated(subset=["id"]).sum())
    print(f"Duplicate IDs found: {dupes}")
    df = df.drop_duplicates(subset=["id"])
    bad = df[(df["value"] < 0) | (df["value"] > 1000)]
    print(f"Out-of-range values found: {len(bad)}")
    df = df[(df["value"] >= 0) & (df["value"] <= 1000)]

    df.to_csv("cleaned_data.csv", index=False)
    print(f"Loaded {len(df)} clean rows to cleaned_data.csv")


if __name__ == "__main__":
    main()