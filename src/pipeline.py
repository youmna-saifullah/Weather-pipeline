import os

import pandas as pd

from src.clean import clean
from src.validate import validate

SOURCE = "data/sample/weather_sample.csv"
OUTPUT = "data/processed/summary.csv"


def run():
    df = clean(pd.read_csv(SOURCE))
    validate(df)
    summary = df.groupby("city", as_index=False).agg(readings=("temp", "count"), avg_temp=("temp", "mean"))
    summary["avg_temp"] = summary["avg_temp"].round(1)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    summary.to_csv(OUTPUT, index=False)
    print(summary.to_string(index=False))
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    run()
