from src.data import DATA
from src.l import l

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
    t, evals = DATA("../data/auto93.csv").tree(True)
    clusters = t.getClusters()
    print("evals: ", evals)
    print("cluster: ", clusters)

    for cluster in clusters:
        print("Cluster:", cluster.data.cols.names)
        print( "Centroid:", l().o(cluster.data.mid().cells))
        print("Rows:", cluster.data.rows)
        for row in cluster.data.rows:
            print(row.cells)
        print("=====================================")
        for _ in range(len(cluster.data.rows)//3):

            shuffled_rows = list(cluster.data.rows)
            random.shuffle(shuffled_rows)
        
            # Picking three random rows without replacement
            a, b, c = shuffled_rows[:3]

            print("a:", a.cells)
            print("b:", b.cells)
            print("c:", c.cells)
            print("Mutated:", vectorMutate(a.cells, b.cells, c.cells))
        
        print("=====================================")


