from src.data import DATA

def tree():
    t, evals = DATA("../data/auto93.csv").tree(True)
    t.show()
    print("evals: ", evals)

