import pandas as pd

def check_data_type(value):
    try:
        # Try to convert the value to int
        int(value)
        return 'int'
    except ValueError:
        try:
            # Try to convert the value to float
            float(value)
            return 'float'
        except ValueError:
            # Otherwise, consider it as string
            return 'str'

def typecast_column(df, column):
    data_type = check_data_type(df[column][0])
    if data_type == 'int':
        df[column] = df[column].astype(int)
    elif data_type == 'float':
        df[column] = df[column].astype(float)
    return df

def typeChecker(input_csv_file, output_csv_file):
    # input_csv_file = "../data/auto93.csv"
    # output_csv_file = "../data/mutated_auto93.csv"

    # Read the CSV file
    df = pd.read_csv(input_csv_file)

    # Typecast each column to the same data type
    for column in df.columns:
        df = typecast_column(df, column)

    # Save the mutated CSV
    df.to_csv(output_csv_file, index=False)
    print("Mutated CSV file saved successfully.")
