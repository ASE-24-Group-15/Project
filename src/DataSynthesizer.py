from DataSynthesizer.DataDescriber import DataDescriber
from DataSynthesizer.DataGenerator import DataGenerator
from DataSynthesizer.ModelInspector import ModelInspector
import pandas as pd

# Load the original dataset
original_data = pd.read_csv("../data/auto93.csv")

# Initialize and fit the data describer
describer = DataDescriber()
describer.describe_dataset_in_correlated_attribute_mode(original_data)

# Generate the synthesized dataset
generator = DataGenerator()
synthesized_data = generator.generate_dataset_in_correlated_attribute_mode(describer.data_description)

# Save the synthesized dataset to a CSV file
synthesized_data.to_csv("../mutated_data/DataSyntesizer/auto93_synthesized_dataset.csv", index=False)

# Optionally, inspect the model
inspector = ModelInspector(original_data, synthesized_data)
inspector.mutual_information_heatmap()
