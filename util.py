import base64
import io
import numpy as np
import pandas as pd

from pathlib import Path

def select_columns(data: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Selects the given columns from the DataFrame."""
    return data[columns]

def extract_columns(data: pd.DataFrame) -> np.array:
    """Extracts the column names from the given DataFrame."""
    return data.columns.values

def decode(contents: str) -> io.StringIO:
    """Decodes the file content string."""
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    decoded = io.StringIO(decoded.decode('utf-8'))
    return decoded

def read_csv(data: io.StringIO, nrows: int=None) -> pd.DataFrame:
    """Reads a CSV from the data uploaded. 
    Can control the amount of lines read using the nrows parameter.
    """
    df = pd.read_csv(data, nrows=nrows)
    return df

def is_valid_format(filename: str) -> bool:
    """Checks if the file is a valid format (it supports only CSV files)."""
    path = Path(filename)
    format = path.suffix.lower()
    return True if format == '.csv' else False

def parse_contents(contents: str) -> pd.DataFrame:
    """Parses the uploaded file and convert it to a DataFrame."""
    csv = decode(contents)
    df = read_csv(csv, nrows=1)
    return df