from src.tricks import csv
from src.row import ROW
from src.cols import COLS
from src.l import l
import src.config as config 
from src.node import NODE
import random

class DATA:
    def __init__(self, src, fun = None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for x in csv(src):
                self.add(x, fun)
        elif src is not None:
            for x in src:
                self.add(x, fun)
        
    def add(self, t, fun=None):
        row = t if not isinstance(t, list) and t.cells else ROW(t)
        if self.cols:
            if(fun):
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row)
    
    def mid(self, cols=None):
        u = []
        for col in cols or self.cols.all.values():
            u.append(col.mid())
        return ROW(u)
    
    def div(self, cols=None):
        u = []
        for col in cols or self.cols.all.values():
            u.append(col.div())
        return ROW(u)

    def stats(self, cols = None, fun = None, ndivs = None):
        u = {".N" : len(self.rows)}
        targetCols = getattr(self.cols, fun or "y")
        for col in targetCols:
            u[targetCols[col].txt] = l().rnd(getattr(targetCols[col], fun or "mid")(), ndivs)
        print(u)
        return u
    
    def gate(self, budget0, budget, some):
        stats, bests = [], []
        rows = l().shuffle(self.rows)
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        
        row1 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:6]]

        row2 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in rows[:50]]

        rows.sort(key=lambda x: x.d2h(self))
        row3 += [[row.cells[i] for i in list(self.cols.y.keys())] for row in [rows[0]]]

        rows = l().shuffle(rows)
        lite = rows[:budget0]
        dark = rows[budget0:]

        for i in range(budget):
            best, rest = self.bestRest(lite, len(lite) ** some)
            todo, selected = self.split(best, rest, lite, dark) 

            sample = [self.cols.names[0][-len(self.cols.y.keys()):]] 
            random_sample = random.sample(dark, k=budget0+i)
            for d in random_sample:
                sample.append(d.cells[-len(self.cols.y.keys()):])
            rand_centroid = DATA(sample).mid() 
            row4.append(rand_centroid.cells)

            sample = [self.cols.names[0][-len(self.cols.y.keys()):]] 
            for d in selected.rows:
                sample.append(d.cells[-len(self.cols.y.keys()):])
            mid_centroid = DATA(sample).mid() 
            row5.append(mid_centroid.cells)

            # top_row_values = [[best.cells[i] for i in list(self.cols.y.keys())] for best in bests[:1]]

            dark.pop(todo)

            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))
        
            row6.append(bests[0].cells[-len(self.cols.y.keys()):])

        # return stats, bests, row1, row2, row3, row4, row5, row6
        return stats, bests
            
    def bestRest(self, rows, want):
        rows = sorted(rows, key=lambda x: x.d2h(self))
        best, rest = self.cols.names[:], self.cols.names[:]
        for i, row in enumerate(rows):
            if i < want:
                best.append(row)
            else:
                rest.append(row)
        return DATA(best), DATA(rest)
    
    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names)
        max = 1E30
        out = 0
        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2)
            r = row.like(rest, len(lite), 2)
            if b > r :
                selected.add(row)
            tmp = abs(b+r) / abs(b -r + 1E-300)
            if tmp > max:
                out, max = i, tmp
        return out, selected
    
    def farapart(self, rows, sortp=False, a=None):
        rows = rows or self.rows 
        far = int(len(rows) *  config.the.get("Far", 0.95))
        evals = 1 if a else 2
        if not a:
            a = l().any(rows).neighbors(self, rows)[far]
        b = a.neighbors(self, rows)[far]

        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a

        return a, b, a.dist(b, self), evals
    
    # Optimization via tecursive random projects. 
    # `Half` then data, then recurse on the best half. 
    def branch(self, stop=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals, rest
            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _ = self.half(data.rows, True, above)
                evals += 1
                rest.extend(rights)
                return _branch(self.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals

        return _branch(self)
    
    # Divide `rows` into two halves, based on distance to two far points.
    def half(self, rows, sortp=False, before=None, evals=None):
        evals = evals or 0
        some = l().many(rows, min(config.the.Half, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)
        
        def d(row1, row2):
            return row1.dist(row2, self)

        def project(r):
            return ((d(r, a) ** 2) + (C ** 2) - (d(r, b) ** 2)) / (2 * C)

        sorted_rows = sorted(rows, key=project)
        
        mid_index = len(sorted_rows) // 2
        a_s = sorted_rows[:mid_index]
        b_s = sorted_rows[mid_index:]

        return a_s, b_s, a, b, C, d(a, b_s[0]), evals

    def clone(self, rows=None):
        new = DATA(self.cols.names)
        if rows is not None:
            for row in rows:
                new.add(row)
        return new
    
    def tree(self, sortp=False):
        evals = 0

        def _tree(data, above=None, lefts=None, rights=None, node=None):
            nonlocal evals
            node = NODE(data)
            if len(data.rows) > 2 * len(self.rows) ** 0.5:
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                evals += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)
            return node

        return _tree(self), evals



    



        