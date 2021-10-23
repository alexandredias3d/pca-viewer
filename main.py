import numpy as np
import pandas as pd
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

if __name__ == '__main__':

    df = pd.read_csv('test.csv')

    d = select_columns(df, ['term1', 'term2', 'term3'])
    nd = normalize_data(d)

    rd = run_pca(nd)

    print()
    