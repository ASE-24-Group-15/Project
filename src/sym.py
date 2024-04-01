import math
import src.config as config

class SYM:
    #Create
    def __init__(self, s= " ", n = 0):
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0
        
    #Update
    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x,0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x 

    #Query 
    def mid(self):
        return self.mode
    
    def div(self):
        e = 0
        for _, v in self.has.items():
            e -= v / self.n * math.log(v / self.n, 2)
        return e

    def small(self):
        return 0
    
    def like(self, x, prior):
        return (self.has.get(x, 0) + config.the.m*prior) / (self.n + config.the.m) if (self.n + config.the.m) != 0 else 0
    
    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        return 0 if x == y else 1

    def bin(self, x):
        return x