from src.data import DATA
import csv
import src.config as config
import src.typeChecker as typeChecker
from src.classify import classify
from src.smape import smape
import src.KL_divergence as kl
from src.privacy_score import privacy_preservation_score
import random
import os
import numpy as np
from src.metrics import js_knn

F = 0.5  # Example value for F
CF = 0.8  # Example value for CF

def delta(a, b, c):
    return a + F * abs(b - c)

def crossover(a, b, c):
    return delta(a, b, c) if random.random() < CF else a

def vectorMutate(a, b, c):
    return [crossover(int(a[i])if a[i]!='?' else 0, int(b[i])if b[i]!='?' else 0, int(c[i]) if c[i]!='?' else 0) for i in range(len(a))]


def cluster(iterations = 1 , iterator = 'n12'):
    randList = []
    bestList = []
    smapeList = []
    kl_divergence = []
    privacy_score = []
    Js = []

    t, _ = DATA(config.the.file).tree(True, iterator)
    clusters = t.getClusters()

    for iteration in range(iterations):
        mutated_values= []

        for cluster in clusters:
            for a in cluster.data.rows:
                shuffled_rows = [row for row in cluster.data.rows if row != a]
                random.shuffle(shuffled_rows)
                b, c = shuffled_rows[:2] # Picking two random rows without replacement
                mutated_values.append(vectorMutate(a.cells, b.cells, c.cells))

        # Define the directory to save the CSV files
        output_directory = f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/{iterator}/"

        # Create the directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)

        # Mutated file name
        csv_filename = f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/{iterator}/{config.the.file.split('/')[-1].split('.')[0]}_mutated_{iteration + 1}.csv"

        # Write the data to the CSV file
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(t.data.cols.names[0])
            for row in mutated_values:
                writer.writerow(row)

        # check the type of the mutated file
        typeChecker.typeChecker(config.the.file, csv_filename)

        #scoring the mutated file
        #calculate smape score
        smapeList.append(smape(config.the.file, csv_filename))

        # Calculating the privcacy score
        privacy_score.append(np.mean(privacy_preservation_score(config.the.file, csv_filename)))
        mutated_data = DATA(csv_filename)

        # Scott-Knott for statistical analysis
        _, best = mutated_data.gate(4, 16, 0.5)
        bestList.append(best[-1].d2h(mutated_data))

        randRows = random.sample(mutated_data.rows, 20)
        rows = sorted(randRows, key=lambda x: x.d2h(mutated_data))
        randList.append(rows[0].d2h(mutated_data))

        # JSD score
        Js.append(js_knn(config.the.file, csv_filename))

        #classify the mutated file to check the model performance
        classify(csv_filename)

        # Column wise divergence score
        # kl_divergence.append(list(kl.calculate_kl_divergence(config.the.file, csv_filename).values()))

    print("Best List: ", bestList)
    print("Random List: ", randList)
    print("SMAPE List: ", smapeList)
    print("KL Divergence: ", kl_divergence)
    print("Privacy Score: ", privacy_score)
    print("JSD: ", Js)
    return bestList, randList, smapeList, kl_divergence, privacy_score, Js


