import base64
import io
import numpy as np
import pandas as pd

from pathlib import Path

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

def is_valid_format(filename: str) -> bool:
    path = Path(filename)
    format = path.suffix.lower()
    return True if format == '.csv' else False

def parse_contents(contents):
    csv = decode(contents)
    df = read_csv(csv, nrows=1)
    columns = extract_columns(df)

    options = [{'label': column, 'value': index} for index, column in enumerate(columns)]

    return options, options