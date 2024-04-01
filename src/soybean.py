from src.learn import learn 
from src.data import DATA
import src.config as config

#Test on Soybean
def eg_km():
    print("#{:4s}\t{}\t{}".format("acc", "k", "m"))
    for k in range(4):
        config.the.k = k
        for m in range(4):
            config.the.m = m
            wme = {"acc": 0, "datas": {}, "tries": 0, "n": 0}
            DATA("../data/soybean.csv", lambda data, t: learn(data, t, wme))
            print("{:5.2f}\t{}\t{}".format(wme["acc"] / wme["tries"], k, m))

