import pandas as pd


def clean(df):
    """Tidy city names, make temperature a number, drop bad and repeated rows."""
    df = df.copy()
    df["city"] = df["city"].str.strip().str.title()
    df["temp"] = pd.to_numeric(df["temp"], errors="coerce")
    df = df.dropna(subset=["temp"]).drop_duplicates()
    return df.reset_index(drop=True)
