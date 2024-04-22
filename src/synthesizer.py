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

    def bonr(n):
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


    classify(config.the.file)
    print("n12")
    smapeList_n12,privacy_score_n12,js_score_n12 = external(config.the.file, "n12")
    print("n12 JS avg: ", sum(js_score_n12)/len(js_score_n12))
    print("cube")
    smapeList_cube,privacy_score_cube,js_score_cube = external(config.the.file, "cube")
    print("cube JS avg: ", sum(js_score_cube)/len(js_score_cube))
    print("square")
    smapeList_square, privacy_score_square,js_score_square = external(config.the.file, "square")
    print("square JS avg: ", sum(js_score_square)/len(js_score_square))
    for iteration in range(20):
        classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/HowSo/synthetic_data_mutated_{iteration + 1}.csv")
        classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/correlated_attribute_mode/synthetic_data_mutated_{iteration + 1}.csv")
        classify(f"../mutated_data/{config.the.file.split('/')[-1].split('.')[0]}/independent_attribute_mode/synthetic_data_mutated_{iteration + 1}.csv")
    print("howso")
    howso_smapeList, howso_privacy_score, howso_js_score = external(config.the.file, "howso")
    print("howso JS avg: ", sum(howso_js_score)/len(howso_js_score))
    print("correlated_attribute_mode")
    DS_corr_smapeList, DS_corr_privacy_score, DS_corr_js_score = external(config.the.file, "correlated_attribute_mode")
    print("correlated_attribute_mode JS avg: ", sum(DS_corr_js_score)/len(DS_corr_js_score))
    print("independent_attribute_mode")
    DS_incorr_smapeList, DS_incorr_privacy_score, DS_incorr_js_score = external(config.the.file, "independent_attribute_mode")
    print("independent_attribute_mode JS avg: ", sum(DS_incorr_js_score)/len(DS_incorr_js_score))

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
            ])'''
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
    
    # print("KL Divergence Statistics:")
    # eg0([   
    #         SAMPLE(kl_divergence_n12, "kl_divergence_n12"),
    #         SAMPLE(kl_divergence_cube, "kl_divergence_cube"),
    #         SAMPLE(kl_divergence_square, "kl_divergence_square")
    #         ])