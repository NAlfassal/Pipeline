import pandas as pd


def require_columns(df: pd.DataFrame, cols: list[str]) -> None :
    missing_cols = [col for col in cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

def assert_non_empty(df: pd.DataFrame, name: str = "df") -> None:
    if df.empty:
        raise ValueError(f"The DataFrame '{name}' is empty.")

def assert_unique_key(df: pd.DataFrame, key: str, *, allow_na: bool = False) -> None:
    if not allow_na:
        assert df[key].notna().all(), f"{key} contains NA"
    dup = df[key].duplicated(keep=False) & df[key].notna()
    assert not dup.any(), f"{key} not unique; {dup.sum()} duplicate rows"

def assert_in_range(s: pd.Series, lo=None, hi=None, name: str = "value") -> None:
    values = s.dropna()
    if lo is not None:
        if (values < lo).any():
            raise AssertionError(f"{name} has values below {lo}")
    if hi is not None:
        if (values > hi).any():
            raise AssertionError(f"{name} has values above {hi}")
