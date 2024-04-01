from src.data import DATA
from src.l import l

def branch():
    d = DATA("../data/auto93.csv")
    best, rest, evals = d.branch()
    print("Best Cluster - Centroid: ", l().o(best.mid().cells))
    print("Rest Cluster - Centroid: ", l().o(rest.mid().cells))
    print("evals: ",evals)
    
