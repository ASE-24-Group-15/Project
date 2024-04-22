import os
import numpy as np
from src.classify import classify
from src.smape import smape
from src.privacy_score import privacy_preservation_score
from src.metrics import js_knn
import src.config as config
from src.KNN import knn

smapeList = []
privacy_score = []
Js = []
knn_accuracy = []
knn_recall = []
knn_precision = []
knn_f1 = []
knn_mcc = []

def external(file, folder_path):

    # Run the process 20 times
    for iteration in range(20):
        # Iterate over each file in the folder
        # Create the full file path
        if folder_path == "n12":
            csv_filename = f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/n12/{config.the.file.split('/')[-1].split('.')[0]}_mutated_{iteration + 1}.csv"
        elif folder_path == "cube":
            csv_filename = f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/cube/{config.the.file.split('/')[-1].split('.')[0]}_mutated_{iteration + 1}.csv"
        elif folder_path == "square":
            csv_filename = f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/square/{config.the.file.split('/')[-1].split('.')[0]}_mutated_{iteration + 1}.csv"
        else:
            csv_filename = f"../mutated_data/{file.split('/')[-1].split('.')[0]}/{folder_path}/synthetic_data_mutated_{iteration + 1}.csv"

        # Perform the operations
        smapeList.append(smape(file, csv_filename))
        privacy_score.append(np.mean(privacy_preservation_score(file, csv_filename)))
        Js.append(js_knn(file, csv_filename))
        knn_accuracy.append(knn(file, csv_filename)[0])
        knn_recall.append(knn(file, csv_filename)[1])
        knn_precision.append(knn(file, csv_filename)[2])
        knn_f1.append(knn(file, csv_filename)[3])
        knn_mcc.append(knn(file, csv_filename)[4])

        # classify(csv_filename)
    return smapeList, privacy_score, Js, knn_accuracy, knn_recall, knn_precision, knn_f1, knn_mcc