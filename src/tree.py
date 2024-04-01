from src.data import DATA
from src.l import l

def tree():
    t, evals = DATA("../data/auto93.csv").tree(True)
    t.show()
    print("evals: ", evals)

