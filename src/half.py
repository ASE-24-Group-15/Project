from src.data import DATA
from src.l import l

def half():
    d = DATA("../data/auto93.csv")

    lefts, rights, left, right, C, cut, _ = d.half(d.rows)
    o = l().o

    print("The best cut is at", o(cut))
    print("The left cluster has", o(len(lefts)))
    print("The left cluster has", o(len(left.cells)))
    print("The right cluster has", o(len(rights)))
    print("The right cluster has", o(len(right.cells)))
    print("The distance between the centroids is", o(C))
    
