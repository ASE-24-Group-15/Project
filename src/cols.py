from src.num import NUM
from src.sym import SYM

class COLS:
    #Create
    def __init__(self, row):
        klass, col = None, None
        x,y,all = {}, {}, {}

        # if not isinstance(row.cells, list):
        #     row.cells = list(row.cells)
        for at, txt in enumerate(row.cells):
            col = (NUM if txt[0].isupper() else SYM)(txt, at)
            all[len(all)] = col 
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    klass = col 
                (y if txt[-1] in "!+-" else x)[at] = col
        self.x = x 
        self.y = y
        self.all = all
        self.klass = klass
        self.names = [row.cells]
    
    #Update
    def add(self, row):
        for cols in [self.x, self.y]:
            for _, col in cols.items():
                col.add(row.cells[col.at])
        return row