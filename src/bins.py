from src.data import DATA
from src.l import l
import src.config as config 
from src.ranges import ranges1

def bins():
    l_instance = l()
    d = DATA("../data/auto93.csv")
    best, rest, _ = d.branch()
    # LIKE = [row.cells for row in best.rows]
    LIKE = best.rows
    HATE = l_instance.many(l_instance.shuffle(rest.rows), 3 * len(LIKE))

    def score(range):
        return range.score("LIKE", len(LIKE), len(HATE))
    
    t = []
    for col in d.cols.x.values():
        print("")
        for range in ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
            print(l_instance.o(range))
            t.append(range)
    
    t.sort(key=lambda x: score(x), reverse=True)
    max_score = score(t[0])

    print("\n#scores:\n")
    for v in t[1:config.the.get("Beam")]:
        if score(v) > max_score * 0.1:
            print("score:", l_instance.rnd(score(v)), l_instance.o(v))
    
    print({"LIKE": len(LIKE), "HATE": len(HATE)})
