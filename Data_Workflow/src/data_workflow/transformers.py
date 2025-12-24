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
#def apply_mapping(s: pd.Series, mapping: dict[str, str]) -> pd.Series:
     #- Map values using a dictionary
     #- Values not in mapping stay unchanged