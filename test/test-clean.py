import pandas as pd

from src.clean import clean


def test_city_names_are_tidied():
    df = pd.DataFrame({"city": [" lahore ", "KARACHI"], "temp": [30, 31]})
    assert list(clean(df)["city"]) == ["Lahore", "Karachi"]


def test_missing_temperature_is_dropped():
    df = pd.DataFrame({"city": ["A", "B"], "temp": [30, None]})
    assert len(clean(df)) == 1


def test_duplicates_are_removed():
    df = pd.DataFrame({"city": ["A", "A"], "temp": [30, 30]})
    assert len(clean(df)) == 1
