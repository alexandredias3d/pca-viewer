import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from util import *

def normalize_data(data: pd.DataFrame) -> np.array:
    """Normalizes the pandas DataFrame using the StandardScaler."""
    std_scaler = StandardScaler().fit(data)
    normalized_data = std_scaler.transform(data)

    return normalized_data
    
def run_pca(data: np.array) -> np.array:
    """Run the PCA algorithm and takes at most 3 components to visualize."""
    _, columns = data.shape
    k = min(3, columns)

    pca = PCA(n_components=k).fit(data)
    reduced_data = pca.transform(data)

    return reduced_data

def extract_values(array: np.array) -> tuple[np.array, np.array, np.array]:
    """Extracts 2 or 3 dimensions from the reduced data found by the PCA algorithm."""
    x = array[:, 0]
    y = array[:, 1]
    z = None
    if is_3d(array):
        z = array[:, 2]

    return x, y, z

def is_3d(array: np.array) -> bool:
    """Checks if the given array has 3 dimensions (columns)."""
    return True if array.shape[1] == 3 else False

def has_color(color: int) -> bool:
    """Checks if the user has selected one column to use as the color."""
    return True if color else False

def plot(array: np.array, color: np.array=None) -> dict:
    """Makes a scatter plot of the data."""
    x, y, z = extract_values(array)    

    if is_3d(array):
        fig = px.scatter_3d(x=x, y=y, z=z, color=color)
    else:
        fig = px.scatter(x=x, y=y, color=color)

    return fig