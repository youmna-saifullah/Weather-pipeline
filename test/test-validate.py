import pandas as pd
import pytest

from src.validate import validate


def good():
    return pd.DataFrame({"city": ["A"], "temp": [25.0], "humidity": [50]})


def test_good_data_passes():
    assert validate(good())


def test_impossible_temperature_fails():
    df = good()
    df.loc[0, "temp"] = 300
    with pytest.raises(AssertionError):
        validate(df)


def test_impossible_humidity_fails():
    df = good()
    df.loc[0, "humidity"] = 140
    with pytest.raises(AssertionError):
        validate(df)
