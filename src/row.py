import math
# import sys
import src.config as config

class ROW:
    def __init__(self, t):
        self.cells = t

    # Return the ‘data‘ (from ‘datas‘) that I like the best
    def likes(self, datas):
        n, nHypotheses = 0, 0
        for k, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1
        most = None
        out = None
        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most == None or abs(tmp) > abs(most):
                most, out = tmp, k
        return out, most

    # How much does ROW like `self`. Using logs since these 
    # numbers are going to get very small.
    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + config.the.k) / (n + config.the.k * nHypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                if abs(inc) != 0:
                    out = out + math.log(inc)
                else:
                    out = out  +  float('-inf')
        return math.exp(1) ** out
    
    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y.values():
            # x = self.cells.get(col.at)
            # if x is None:
            #     sys.stderr.write("?")
            # else:
            n = n + 1
            d = d + abs(col.heaven - col.norm(self.cells[col.at])) ** 2
        return d ** .5 / n ** .5

    def dist(self, row, data):
        d, n, p = 0, 0, config.the.p
        for col in data.cols.x.values():
            n += 1
            d += col.dist(self.cells[col.at], row.cells[col.at]) ** p
        return (d ** (1 / p) / n ** (1 / p)) 

    def neighbors(self, data, rows=None):
        rows = rows or data.rows
        return sorted(rows, key=lambda row: self.dist(row, data))
