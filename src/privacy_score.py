import pandas as pd
import numpy as np

def load_data(original_file, synthesized_file):
    original_data = pd.read_csv(original_file).replace('?',0)
    synthesized_data = pd.read_csv(synthesized_file).replace('?',0)
    return original_data, synthesized_data

def calculate_distances(original_data, synthesized_data):
    distances = []
    for xsyn in synthesized_data.values:
        # Calculate distances between xsyn and all points in original_data
        dist = np.linalg.norm(original_data.values - xsyn, axis=1)
        distances.append(dist)
    return np.array(distances)

def calculate_knn_distances(distances, k=5):
    knn_distances = []
    for dist in distances:
        # Sort distances and select the k nearest neighbors
        knn_dist = np.sort(dist)[:k]
        knn_distances.append(knn_dist)
    return np.array(knn_distances)

def calculate_privacy_score(distances, knn_distances):
    privacy_scores = []
    for i in range(len(distances)):
        d = distances[i].min()  # distance to the nearest original neighbor
        dmin = knn_distances[i][1]  # second smallest distance among k nearest neighbors
        privacy_score = d / dmin
        privacy_scores.append(privacy_score)
    return privacy_scores

def privacy_preservation_score(original_file, synthesized_file):

    original_data, synthesized_data = load_data(original_file, synthesized_file)
    distances = calculate_distances(original_data.astype(float), synthesized_data.astype(float))
    knn_distances = calculate_knn_distances(distances)
    privacy_scores = calculate_privacy_score(distances, knn_distances)

    print("Privacy Scores:")
    print("Statistical Details of Privacy Scores:")
    print(f"Minimum: {np.min(privacy_scores)}")
    print(f"Maximum: {np.max(privacy_scores)}")
    print(f"Mean: {np.mean(privacy_scores)}")
    print(f"Standard Deviation: {np.std(privacy_scores)}")
    print(f"Average: {np.mean(privacy_scores)}")

    return privacy_scores
