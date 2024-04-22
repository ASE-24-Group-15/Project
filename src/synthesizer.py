from src.cluster import cluster    
import src.config as config
from src.data import DATA
from src.stats import eg0, SAMPLE
from src.external_Score import external
from datetime import datetime
import random
from src.classify import classify

def synthesizer():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")
    print("seed : ", config.the.seed)
    data = DATA(config.the.file)
    print("rows : ", len(data.rows))
    print("cols : ", len(data.cols.names[0]))
    print("names \t\t\t\t", '[' + ', '.join(["'" + item + "'" for item in data.cols.names[0]]) + ']' + "\t\td2h-")
    print("Statistics")

    '''def bonr(n):
        bestList = []
        for i in range(n):
            data = DATA(config.the.file)
            _, best = data.gate(4, n-4, 0.5)
            bestList.append(best[-1].d2h(data))
        return bestList

    def rand(n):
        randList = []
        for i in range(n):
            data = DATA(config.the.file)
            randRows = random.sample(data.rows, n)
            rows = sorted(randRows, key=lambda x: x.d2h(data))
            randList.append(rows[0].d2h(data))
        return randList

    
    # bonr_20_n12, rand_20_n12, smapeList_n12, kl_divergence_n12, privacy_score_n12, js_score_n12 = cluster(5)
    # bonr_20_cube, rand_20_cube, smapeList_cube, kl_divergence_cube, privacy_score_cube, js_score_cube = cluster(5, "cube")
    # bonr_20_square, rand_20_square, smapeList_square, kl_divergence_square, privacy_score_square, js_score_square = cluster(5, "square")


    # bonr_20_n12, rand_20_n12, smapeList_n12,privacy_score_n12,js_score_n12 = cluster(20)
    # bonr_20_cube, rand_20_cube, smapeList_cube,privacy_score_cube,js_score_cube = cluster(20, "cube")
    # bonr_20_square, rand_20_square, smapeList_square, privacy_score_square,js_score_square = cluster(20, "square")
    # org_bonr_20, org_rand_20 = bonr(20), rand(20)


    # classify(config.the.file)
    
    # for iteration in range(20):
    #     classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/HowSo/synthetic_data_mutated_{iteration + 1}.csv")
    #     classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/correlated_attribute_mode/synthetic_data_mutated_{iteration + 1}.csv")
    #     classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/independent_attribute_mode/synthetic_data_mutated_{iteration + 1}.csv")
    '''
    print("n12")
    smapeList_n12,privacy_score_n12,js_score_n12, knn_accuracy_n12, knn_recall_n12, knn_precision_n12, knn_f1_n12, knn_mcc_n12 = external(config.the.file, "n12")
    print("n12 JS avg: ", sum(js_score_n12)/len(js_score_n12))
    
    print("cube")
    smapeList_cube,privacy_score_cube,js_score_cube, knn_accuracy_cube, knn_recall_cube, knn_precision_cube, knn_f1_cube, knn_mcc_cube = external(config.the.file, "cube")
    print("cube JS avg: ", sum(js_score_cube)/len(js_score_cube))
    
    print("square")
    smapeList_square, privacy_score_square,js_score_square, knn_accuracy_square, knn_recall_square, knn_precision_square, knn_f1_square, knn_mcc_square = external(config.the.file, "square")
    print("square JS avg: ", sum(js_score_square)/len(js_score_square))
    
    print("howso")
    howso_smapeList, howso_privacy_score, howso_js_score, howso_knn_accuracy, howso_knn_recall, howso_knn_precision, howso_knn_f1, howso_knn_mcc = external(config.the.file, "howso")
    print("howso JS avg: ", sum(howso_js_score)/len(howso_js_score))
    
    print("correlated_attribute_mode")
    DS_corr_smapeList, DS_corr_privacy_score, DS_corr_js_score, DS_corr_knn_accuracy, DS_corr_knn_recall, DS_corr_knn_precision, DS_corr_knn_f1, DS_corr_knn_mcc = external(config.the.file, "correlated_attribute_mode")
    print("correlated_attribute_mode JS avg: ", sum(DS_corr_js_score)/len(DS_corr_js_score))
    
    print("independent_attribute_mode")
    DS_incorr_smapeList, DS_incorr_privacy_score, DS_incorr_js_score, DS_incorr_knn_accuracy, DS_incorr_knn_recall, DS_incorr_knn_precision, DS_incorr_knn_f1, DS_incorr_knn_mcc = external(config.the.file, "independent_attribute_mode")
    print("independent_attribute_mode JS avg: ", sum(DS_incorr_js_score)/len(DS_incorr_js_score))

    print("SMAPE Statistics:")
    eg0([   
            SAMPLE(smapeList_n12, "smapeList_n12"),
            SAMPLE(smapeList_cube, "smapeList_cube"),
            SAMPLE(smapeList_square, "smapeList_square"),
            SAMPLE(howso_smapeList, "howso_smapeList"),
            SAMPLE(DS_corr_smapeList, "DS_corr_smapeList"),
            SAMPLE(DS_incorr_smapeList, "DS_incorr_smapeList")
            ])
    
    print("Privacy Score Statistics:")
    eg0([   
            SAMPLE(privacy_score_n12, "privacy_score_n12"),
            SAMPLE(privacy_score_cube, "privacy_score_cube"),
            SAMPLE(privacy_score_square, "privacy_score_square"),
            SAMPLE(howso_privacy_score, "howso_privacy_score"),
            SAMPLE(DS_corr_privacy_score, "DS_corr_privacy_score"),
            SAMPLE(DS_incorr_privacy_score, "DS_incorr_privacy_score")
            ])
    
    print("JSD Statistics:")
    eg0([   
            SAMPLE(js_score_n12, "js_score_n12"),
            SAMPLE(js_score_cube, "js_score_cube"),
            SAMPLE(js_score_square, "js_score_square"),
            SAMPLE(howso_js_score, "howso_js_score"),
            SAMPLE(DS_corr_js_score, "DS_corr_js_score"),
            SAMPLE(DS_incorr_js_score, "DS_incorr_js_score")
            ])
    
    print("KNN Accuracy Statistics:")
    eg0([   
            SAMPLE(knn_accuracy_n12, "knn_accuracy_n12"),
            SAMPLE(knn_accuracy_cube, "knn_accuracy_cube"),
            SAMPLE(knn_accuracy_square, "knn_accuracy_square"),
            SAMPLE(howso_knn_accuracy, "howso_knn_accuracy"),
            SAMPLE(DS_corr_knn_accuracy, "DS_corr_knn_accuracy"),
            SAMPLE(DS_incorr_knn_accuracy, "DS_incorr_knn_accuracy")
            ])
    
    print("KNN Recall Statistics:")
    eg0([   
            SAMPLE(knn_recall_n12, "knn_recall_n12"),
            SAMPLE(knn_recall_cube, "knn_recall_cube"),
            SAMPLE(knn_recall_square, "knn_recall_square"),
            SAMPLE(howso_knn_recall, "howso_knn_recall"),
            SAMPLE(DS_corr_knn_recall, "DS_corr_knn_recall"),
            SAMPLE(DS_incorr_knn_recall, "DS_incorr_knn_recall")
            ])
    
    print("KNN Precision Statistics:")
    eg0([   
            SAMPLE(knn_precision_n12, "knn_precision_n12"),
            SAMPLE(knn_precision_cube, "knn_precision_cube"),
            SAMPLE(knn_precision_square, "knn_precision_square"),
            SAMPLE(howso_knn_precision, "howso_knn_precision"),
            SAMPLE(DS_corr_knn_precision, "DS_corr_knn_precision"),
            SAMPLE(DS_incorr_knn_precision, "DS_incorr_knn_precision")
            ])
    
    print("KNN F1 Statistics:")
    eg0([   
            SAMPLE(knn_f1_n12, "knn_f1_n12"),
            SAMPLE(knn_f1_cube, "knn_f1_cube"),
            SAMPLE(knn_f1_square, "knn_f1_square"),
            SAMPLE(howso_knn_f1, "howso_knn_f1"),
            SAMPLE(DS_corr_knn_f1, "DS_corr_knn_f1"),
            SAMPLE(DS_incorr_knn_f1, "DS_incorr_knn_f1")
            ])
    
    print("KNN MCC Statistics:")
    eg0([   
            SAMPLE(knn_mcc_n12, "knn_mcc_n12"),
            SAMPLE(knn_mcc_cube, "knn_mcc_cube"),
            SAMPLE(knn_mcc_square, "knn_mcc_square"),
            SAMPLE(howso_knn_mcc, "howso_knn_mcc"),
            SAMPLE(DS_corr_knn_mcc, "DS_corr_knn_mcc"),
            SAMPLE(DS_incorr_knn_mcc, "DS_incorr_knn_mcc")
            ])
    
    '''print("Data Statistics:")
    eg0([   
            SAMPLE(org_bonr_20, "org_bonr_20"),
            SAMPLE(org_rand_20, "org_rand_20"),
            SAMPLE(bonr_20_n12, "bonr_20_n12"),
            SAMPLE(rand_20_n12, "rand_20_n12"),
            SAMPLE(bonr_20_cube, "bonr_20_cube"),
            SAMPLE(rand_20_cube, "rand_20_cube"),
            SAMPLE(bonr_20_square, "bonr_20_square"),
            SAMPLE(rand_20_square, "rand_20_square")
            ])
    print("KL Divergence Statistics:")
    eg0([   
            SAMPLE(kl_divergence_n12, "kl_divergence_n12"),
            SAMPLE(kl_divergence_cube, "kl_divergence_cube"),
            SAMPLE(kl_divergence_square, "kl_divergence_square")
            ])'''