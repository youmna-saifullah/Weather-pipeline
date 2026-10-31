import sys

import pandas as pd


def validate(df):
    """Data quality checks. Raises AssertionError with a clear message if one fails."""
    assert len(df) > 0, "No rows"
    assert df["city"].notna().all(), "City is missing"
    assert df["temp"].between(-60, 60).all(), "Temperature out of range"
    assert df["humidity"].between(0, 100).all(), "Humidity out of range"
    return True


if __name__ == "__main__":
    path = sys.argv[1]
    data = pd.read_csv(path)
    validate(data)
    print(f"OK: {len(data)} rows passed all checks")
