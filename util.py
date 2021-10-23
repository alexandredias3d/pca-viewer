import numpy as np
import pandas as pd

def select_columns(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return data[columns]

def extract_columns(data: pd.DataFrame) -> np.array:
    return data.columns.values