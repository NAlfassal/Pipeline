import pandas as pd

def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(
        order_id=df["order_id"].astype("string"),
        user_id=df["user_id"].astype("string"),
        amount=pd.to_numeric(df["amount"], errors="coerce").astype("Float64"),
        quantity=pd.to_numeric(df["quantity"], errors="coerce").astype("Int64"),
    )
def missingness_report(df: pd.DataFrame) -> pd.DataFrame :
      result = pd.DataFrame({
          'n_missing': df.isna().sum()
      })
      result['p_missing'] = result['n_missing'] / len(df)
      return result.sort_values(by='p_missing', ascending=False)
      

def add_missing_flags(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    for col in cols:
        flag_col = f"{col}_missing"
        df[flag_col] = df[col].isna()
    return df

def normalize_text(s: pd.Series) -> pd.Series:
    import re
    _ws = re.compile(r"\s+")
    return (
        s.astype("string")
        .str.strip()
        .str.casefold()
        .str.replace(_ws, " ", regex=True)
    )

def apply_mapping(s: pd.Series, mapping: dict[str, str]) -> pd.Series:
     return s.map(lambda x: mapping.get(x, x))

def dedupe_keep_latest(df: pd.DataFrame, key_cols: list[str], ts_col: str) -> pd.DataFrame:
    sort_df = df.sort_values(by=ts_col, ascending=False)
    deduped_df = sort_df.drop_duplicates(subset=key_cols, keep="first")
    return deduped_df.sort_index()

def parse_datetime(df: pd.DataFrame, col: str, *, utc: bool = True) -> pd.DataFrame:
    return df.assign(
        **{col: pd.to_datetime(df[col], utc=utc, errors="coerce")}
    )


def add_time_parts(df: pd.DataFrame, ts_col: str) -> pd.DataFrame:
   t = df[ts_col].dt
   return df.assign(
        date=t.date,
        year=t.year,
        month=t.month,
        dow=t.dayofweek, 
        hour=t.hour
    )
                         
def iqr_bounds(s: pd.Series, k: float = 1.5) -> tuple[float, float]:
  Q1 = s.quantile(0.25)
  Q3 = s.quantile(0.75) 
  IQR = Q3 - Q1
  lower_bound = Q1 - k * IQR
  upper_bound = Q3 + k * IQR
  return lower_bound, upper_bound

def winsorize(s: pd.Series, lo: float = 0.01, hi: float = 0.99) -> pd.Series:
    lower = s.quantile(lo)
    upper = s.quantile(hi)
    return s.clip(lower,upper)
    
def add_outlier_flag(df: pd.DataFrame, col: str, *, k: float = 1.5) -> pd.DataFrame:
    low, high = iqr_bounds(df[col], k)
    outlier_check = (df[col] < low) | (df[col] > high)

    return df.assign(
        **{f"{col}_is_outlier": outlier_check}
    )


