import numpy as np
from tqdm import tqdm
from scipy.special import gamma
import pandas as pd

def smape(A, F):
    total = 0.
    bar = tqdm(total=len(A) * len(F))
    for x in A:
        for y in F:
            bar.update(1)
            total += 1./ len(x) * np.sum(2 * np.abs(y - x) / (np.abs(x) + np.abs(y) + np.finfo(float).eps))

    return total / (len(A) * len(F))

def knn_search(X, x, k):
    """
    Custom k-nearest neighbors search function.
    """
    distances = np.linalg.norm(X - x, axis=1)
    indices = np.argsort(distances)[:k]
    return indices, distances[indices]

def js_knn(A_csv_file, F_csv_file, grid_size=100, k=3):
    """
    Based on https://faculty.washington.edu/yenchic/18W_425/Lec7_knn_basis.pdf
    """
    A = pd.read_csv(A_csv_file).replace('?',0).astype(float).values
    F = pd.read_csv(F_csv_file).replace('?',0).astype(float).values
    jsd = 0.
    d = A.shape[1]
    n = A.shape[0]

    Vd = np.pi ** (d / 2) / gamma(d / 2 + 1)

    mins, maxes = np.min([A.min(axis=0), F.min(axis=0)], axis=0), np.max([A.max(axis=0), F.max(axis=0)], axis=0)

    # Generate grid_size points in the range mins to maxes
    grid = np.array([np.linspace(mins[i], maxes[i], grid_size) for i in range(d)]).T
    assert grid.shape == (grid_size, d)

    # Compute KDE for A
    kde_A = []
    for point in grid:
        _, distances = knn_search(A, point, k)
        kde_A.append(k / (n * Vd * distances[-1]))

    kde_A = np.array(kde_A)
    assert kde_A.shape == (grid_size,)

    # Compute KDE for F
    kde_F = []
    for point in grid:
        _, distances = knn_search(F, point, k)
        kde_F.append(k / (n * Vd * distances[-1]))

    kde_F = np.array(kde_F)
    assert kde_F.shape == (grid_size,)

    # Compute JSD
    # First, compute M
    M = (kde_A + kde_F) / 2

    # Now, compute JSD using KL-divergences
    jsd = 0.5 * (np.sum(kde_A * np.log2(kde_A / M)) + np.sum(kde_F * np.log2(kde_F / M)))
    return jsd