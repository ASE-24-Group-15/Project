from src.data import DATA
from src.l import l
import csv
import src.config as config
import src.typeChecker as typeChecker

import random

F = 0.5  # Example value for F
CF = 0.8  # Example value for CF

def delta(a, b, c):
    """
    Calculate the delta value based on the given parameters.

    Parameters:
    a (float): The first value.
    b (float): The second value.
    c (float): The third value.

    Returns:
    float: The delta value calculated using the formula.
    """
    return a + F * (b - c)

def crossover(a, b, c):
    return delta(a, b, c) if random.random() < CF else a

def vectorMutate(a, b, c):
    return [crossover(int(a[i])if a[i]!='?' else 0, int(b[i])if b[i]!='?' else 0, int(c[i]) if c[i]!='?' else 0) for i in range(len(a))]


def cluster():
    # t, _ = DATA("../data/auto93.csv").tree(True)
    t, _ = DATA(config.the.file).tree(True)
    clusters = t.getClusters()
    mutated_values= []

    for cluster in clusters:
        for a in cluster.data.rows:
            shuffled_rows = [row for row in cluster.data.rows if row != a]
            random.shuffle(shuffled_rows)
        
            # Picking two random rows without replacement
            b, c = shuffled_rows[:2]

            mutated_values.append(vectorMutate(a.cells, b.cells, c.cells))

    # Mutated file name
    # csv_filename = "../mutated_data/mutated_auto93.csv"

    csv_filename = "../mutated_data/"+config.the.file.split("/")[-1].split(".")[0]+"_mutated.csv"

    # Write the data to the CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(t.data.cols.names[0])
        for row in mutated_values:
            writer.writerow(row)
    
    typeChecker.typeChecker(config.the.file, csv_filename)

