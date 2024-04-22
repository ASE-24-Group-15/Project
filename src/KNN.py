# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, matthews_corrcoef


# Function to train and evaluate KNN model
def evaluate_knn_model(train_data, test_data):
    # Split data into features and labels
    X_train = train_data.drop(columns=['bin_num'])
    y_train = train_data['bin_num']
    X_test = test_data.drop(columns=['bin_num'])
    y_test = test_data['bin_num']
    
    # Initialize KNN classifier
    knn = KNeighborsClassifier()
    
    # Train the model
    knn.fit(X_train, y_train)
    
    # Make predictions
    y_pred = knn.predict(X_test)
    
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f_score = f1_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)
    
    return accuracy, recall, precision, f_score, mcc

def knn(org_file, mutated):
    # Load original and mutated data
    original_data = pd.read_csv(org_file)
    synthesized_data = pd.read_csv(mutated)
    
    # Train-test split on the original dataset
    _, test_data = train_test_split(original_data, test_size=0.25, random_state=42)
    synthesized_train_data, _ = train_test_split(synthesized_data, test_size=0.25, random_state=42)
    
    # Evaluate KNN model
    accuracy_score, recall_score, precision_score, f1_score, mcc = evaluate_knn_model(synthesized_train_data, test_data)
    
    return accuracy_score, recall_score, precision_score, f1_score, mcc