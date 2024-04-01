import src.config as config
from src.l import l
from src.data import DATA
from src.rules import RULES
from src import ranges

def rules():
    for _ in range(1):
        d = DATA(config.the.file) 
        best0, rest, evals1 = d.branch(config.the.d)
        best, _, evals2 = best0.branch(config.the.D)
        print(evals1 + evals2 + config.the.D - 1)
        LIKE = best.rows
        HATE = l().shuffle(rest.rows)[1:3 * len(LIKE)]
        rowss = {"LIKE": LIKE, "HATE": HATE}
    
        for _, rule in enumerate(RULES(ranges.ranges(d.cols.x, rowss), "LIKE", rowss).sorted):
            result = d.clone(rule.selects(rest.rows))
            if len(result.rows) > 0:
                result.rows.sort(key=lambda a: a.d2h(d))
                print(l().rnd(rule.scored), l().rnd(result.mid().d2h(d)), l().rnd(result.rows[0].d2h(d)),
                      l().o(result.mid().cells), "\t", rule.show())

