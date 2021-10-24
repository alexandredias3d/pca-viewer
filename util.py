import base64
import io
import numpy as np
import pandas as pd

def select_columns(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return data[columns]

def extract_columns(data: pd.DataFrame) -> np.array:
    return data.columns.values

def decode(contents: str) -> io.StringIO:
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    decoded = io.StringIO(decoded.decode('utf-8'))
    return decoded

def read_csv(data: io.StringIO, nrows: int=None) -> pd.DataFrame:
    df = pd.read_csv(data, nrows=nrows)
    return df