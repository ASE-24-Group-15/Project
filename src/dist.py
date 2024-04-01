from src.data import DATA
from src.l import l

def dist():
        d = DATA("../data/auto93.csv")
        r1 = d.rows[0]
        rows = r1.neighbors(d)
        print(f"{'1':<5}{l().o(r1.cells):<40}{l().rnd(r1.dist(r1, d)):<20}")

        for i, row in enumerate(rows, start=1):
            if i % 30 == 0:
                print(f"{i+1:<5}{l().o(row.cells):<40}{l().rnd(row.dist(r1, d)):<20}")

