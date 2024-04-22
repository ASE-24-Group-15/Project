import pandas as pd
import numpy as np
from scipy.stats import entropy

def calculate_kl_divergence(original_csv_file, synthesized_csv_file):
   
    # Read data from CSV files
    original_data = pd.read_csv(original_csv_file).replace('?',0)
    synthesized_data = pd.read_csv(synthesized_csv_file).replace('?',0)

    # Initialize dictionary to store KL divergence values for each column
    kl_divergences = {}

    # Iterate over columns and calculate KL divergence
    for column in original_data.columns:
        original_values = original_data[column].astype(float).values + 1e-30
        synthesized_values = synthesized_data[column].astype(float).values + 1e-30
        # Calculate KL divergence for the current column
        kl_divergences[column] = entropy(original_values, synthesized_values)

    print("KL Divergence Scores:", kl_divergences)
    
    return kl_divergences


'''
import pandas as pd
import numpy as np
from scipy.stats import entropy

def kl_divergence(p, q):
    
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))

# def kl_divergence(a, b):
#     return sum(a[i] * np.log(a[i]/b[i]) for i in range(len(a)))

def calculate_kl_divergence(original_csv_file, synthesized_csv_file):
   
    # Read data from CSV files
    original_data = pd.read_csv(original_csv_file)
    synthesized_data = pd.read_csv(synthesized_csv_file)

    # Initialize dictionary to store KL divergence values for each column
    kl_divergences = {}

    # Iterate over columns and calculate KL divergence
    for column in original_data.columns:
        # Compute histograms for original and synthesized data
        hist_original, bin_edges = np.histogram(original_data[column], bins='auto', density=True)
        hist_synthesized, _ = np.histogram(synthesized_data[column], bins=bin_edges, density=True)

        # Calculate KL divergence for the current column
        # kl_divergences[column] = kl_divergence(hist_original, hist_synthesized)
        
        # kl_divergences[column] = kl_divergence(np.asarray(original_data[column].values),  np.asarray(synthesized_data[column].values))

        kl_divergences[column] = entropy(original_data[column].values, synthesized_data[column].values)

    print("KL Divergence Scores:", kl_divergences)
    
    # return kl_divergences

'''