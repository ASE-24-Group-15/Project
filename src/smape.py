import pandas as pd
from tqdm import tqdm
import numpy as np

def calculate_smape(actual, forecast):
    '''assert len(actual) == len(forecast), "Length of actual and forecast arrays must be the same."

    numerator = 0
    denominator = 0

    for i in range(len(actual)):
        numerator += abs(abs(float(actual[i])) - abs(float(forecast[i])))
        denominator += abs(abs(float(actual[i])) + abs(float(forecast[i])))

    smape = (numerator / denominator) * 200 if denominator != 0 else 0

    return smape'''

    # def smape(A, F):
    A=actual
    F=forecast
    total = 0
    bar = tqdm(total=len(A) * len(F))
    for x in A:
        for y in F:
            bar.update(1)
            x = x.astype(float)
            y = y.astype(float)
            total += 1./ len(x) * np.sum(2 * np.abs(y - x) / (np.abs(x) + np.abs(y) + np.finfo(float).eps))

    return total / (len(A) * len(F))

def smape(input_csv_file, output_csv_file):

    org = pd.read_csv(input_csv_file).replace('?',0)
    df = pd.read_csv(output_csv_file).replace('?',0)
    smape_values = []
    average_smape = calculate_smape(org.values, df.values)
    '''for col in org.columns:
        org_values = org[col]
        df_values = df[col]
        smape_column = calculate_smape(org_values.values, df_values.values)
        print(f"SMAPE for {col}: {smape_column}")
        smape_values.append(smape_column)
        
    average_smape = sum(smape_values) / len(smape_values)'''
    print(f"Average SMAPE across all features: {average_smape}")

    return average_smape

