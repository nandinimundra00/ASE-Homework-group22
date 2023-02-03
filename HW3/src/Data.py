from src.Misc import *
from src.Cols import *
from src.Row import *

class DATA:
    def __init__(self, src=None):
        self.rows = []
        self.cols = None
        fun = lambda x: self.add(x)
        if isinstance(src, str):
            CSV(src, fun)
        elif src:
            for x in src:
                fun(x)

    def add(self, t):
        if hasattr(self, 'cols') and self.cols!=None:
            t = t.cells if hasattr(t, 'cells') else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def clone(self, init=None):
        data = DATA({self.cols.names})
        for x in init or []:
            data.add(x)
        return data

    def stats(self, what=None, cols=None, nPlaces=None):
        def fun(k, col):
            return round(getattr(col, what or "mid")(), nPlaces), col.txt
        return {cols[i].txt: fun(i, cols[i]) for i in range(len(cols))}
