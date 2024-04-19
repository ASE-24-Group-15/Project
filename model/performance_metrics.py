import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, matthews_corrcoef, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from math import sqrt

def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='micro')
    recall = recall_score(y_true, y_pred, average='micro')
    mcc = matthews_corrcoef(y_true, y_pred)
    rmse = sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return accuracy, precision, recall, mcc, rmse, r2

def train_and_test_knn(original_data, mutated_data, target_column):
    # Read original data
    original_df = pd.read_csv(original_data)
    
    # Read mutated data
    mutated_df = pd.read_csv(mutated_data)

    # Split original data into train and test sets
    X_train_orig, X_test_orig, y_train_orig, y_test_orig = train_test_split(
        original_df.drop(target_column, axis=1), 
        original_df[target_column], 
        test_size=0.2, 
        random_state=42
    )
    
    # Split mutated data into train and test sets
    X_train_mutated, X_test_mutated, y_train_mutated, y_test_mutated = train_test_split(
        mutated_df.drop(target_column, axis=1), 
        mutated_df[target_column], 
        test_size=0.2, 
        random_state=42
    )

    # Train KNN classifier on mutated training set
    knn = KNeighborsClassifier()
    knn.fit(X_train_mutated, y_train_mutated)

    # Test KNN classifier on original test set
    y_pred_orig = knn.predict(X_test_orig)

    # Calculate performance metrics
    return calculate_metrics(y_test_orig, y_pred_orig)

def main():
    original_data_folder = input("Enter the path to the folder containing the original dataset: ").strip()
    mutated_data_folder = input("Enter the path to the folder containing the mutated datasets: ").strip()
    target_column = input("Enter the target column name: ").strip()

    # Find the original dataset file in the provided folder
    original_files = [file for file in os.listdir(original_data_folder) if file.endswith('.csv')]
    if len(original_files) != 1:
        print("Error: Found multiple or no original dataset files in the folder.")
        return
    original_data_path = os.path.join(original_data_folder, original_files[0])

    # Find the mutated dataset files in the provided folder
    mutated_files = [file for file in os.listdir(mutated_data_folder) if file.endswith('.csv')]
    if not mutated_files:
        print("Error: No mutated dataset files found in the folder.")
        return

    results = []

    for mutated_file in mutated_files:
        mutated_data_path = os.path.join(mutated_data_folder, mutated_file)
        metrics = train_and_test_knn(original_data_path, mutated_data_path, target_column)
        print(f"Metrics for mutated dataset '{mutated_file}':")
        print("Accuracy:", metrics[0])
        print("Precision:", metrics[1])
        print("Recall:", metrics[2])
        print("MCC:", metrics[3])
        print("RMSE:", metrics[4])
        print("R^2:", metrics[5])
        print()
        results.append([mutated_file] + list(metrics))

    df = pd.DataFrame(results, columns=['Mutated Dataset', 'Accuracy', 'Precision', 'Recall', 'MCC', 'RMSE', 'R^2'])
    df.to_csv('performance_metrics.csv', index=False)

if __name__ == "__main__":
    main()
