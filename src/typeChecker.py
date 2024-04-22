import pandas as pd
import numpy as np

def check_data_type(value):
    if isinstance(value, int) or isinstance(value, np.int64):
        return 'int'
    elif isinstance(value, float) or isinstance(value, np.float64):
        return 'float'
    else: # isinstance(value, str):
        return 'str'

def typecast_column(df, column, org):
    # print("value", org[column][0], "type", type(org[column][0]))
    data_type = check_data_type(org[column][0])
    if data_type == 'int':
        df[column] = df[column].fillna(0).astype(int)
    elif data_type == 'float':
        df[column] = df[column].fillna(0.0).astype(float)
    elif data_type == 'str':
        df[column] = df[column].fillna('').astype(str)
    return df

def typeChecker(input_csv_file, output_csv_file):
    # input_csv_file = "../data/auto93.csv"
    # output_csv_file = "../data/mutated_auto93.csv"

    # Read the CSV file
    org = pd.read_csv(input_csv_file)
    df = pd.read_csv(output_csv_file, na_values='?')

    # Typecast each column to the same data type
    for column in df.columns:
        df = typecast_column(df, column, org)

    # Save the mutated CSV
    df.to_csv(output_csv_file, index=False)
    print("Mutated CSV file saved successfully.")
