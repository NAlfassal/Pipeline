import pandas as pd
def safe_left_join(left: pd.DataFrame, right: pd.DataFrame, on: str, validate: str | list[str], *, suffixes=("_left", "_right")) -> pd.DataFrame:
    return left.merge(
        right,
        on=on,
        how="left",
        validate=validate,
        suffixes=suffixes
    )