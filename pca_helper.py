import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from util import *

def normalize_data(data: pd.DataFrame) -> np.array:
    std_scaler = StandardScaler().fit(data)
    normalized_data = std_scaler.transform(data)

    return normalized_data
    
def run_pca(data: np.array) -> np.array:
    _, columns = data.shape
    k = min(3, columns)

    pca = PCA(n_components=k).fit(data)
    reduced_data = pca.transform(data)

    return reduced_data

def extract_values(array: np.array) -> tuple[np.array, np.array, np.array]:
    x = array[:, 0]
    y = array[:, 1]
    z = None
    if is_3d(array):
        z = array[:, 2]

    return x, y, z

def is_3d(array: np.array) -> bool:
    return True if array.shape[1] == 3 else False

def has_color(color: list[int]) -> bool:
    return True if color >= 0 else False

def plot_pca(array: np.array, colors: np.array=None):
    x, y, z = extract_values(array)    

    if is_3d(array):
        fig = px.scatter_3d(x=x, y=y, z=z, color=colors)
    else:
        fig = px.scatter(x=x, y=y, color=colors)

    return fig