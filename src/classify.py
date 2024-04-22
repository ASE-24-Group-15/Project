from src.data import DATA
import pandas as pd
from src.row import ROW
import src.config as config

def classify(file = None):
        file = file or config.the.file
        d = DATA(file)
        
        best, _, _ = d.branch(1)
        
        r1 = best.rows[0]
        rows = r1.neighbors(d)

        max_distance = rows[-1].dist(r1, d)

        df = pd.read_csv(file)
            
        # Divide the range of distances into 8 equal bins
        bin_size = max_distance / 8
        bins = [i * bin_size for i in range(9)]
        labels = [i+1 for i in range(8)]

        # Iterate over each row, calculate distance, and assign to the appropriate bin
        bin_names = []
        for index, row in df.iterrows():
            row = ROW(row)
            distance = row.dist(r1, d)  # Calculate the distance for the current row
            bin_index = min(int(distance / bin_size), 7)  
            bin_names.append(labels[bin_index])

        # Append the bin information as a new column
        df['bin_num'] = bin_names

        # Save the DataFrame with the new column to a new CSV file
        df.to_csv(file, index=False)