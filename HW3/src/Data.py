from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from operator import itemgetter

class DATA:
    def __init__(self, src=[]):
        self.cols = None
        self.rows = []
        self.n = 0
        if isinstance(src, str):
            self.csv(src)
        else:
            self.add(src)

    def add(self, val):
        if not self.cols:
            self.cols = COLS(val)

        else:
            row = ROW(val)
            self.rows.append(row.cells)
                
            for valX in self.cols.x:
                valX.add(row.cells[valX.at])

            for valY in self.cols.y:
                valY.add(row.cells[valY.at])

    def csv(self, file: str):
        with open(file, "r") as csv:
            filelines = csv.readlines()
            for line in filelines:
                row_split_lines = line.replace("\n", "").rstrip().split(",")
                row_split_lines = [coerce(i) for i in row_split_lines]
                self.add(row_split_lines)
                self.n += len(row_split_lines)

    def stats(self, what, cols, n_places):
        def fun(k, col):
            callable = getattr(col, what)
            return col.rnd(callable(), n_places), col.txt

        return kap(cols, fun)
    
    def better(self, row1, row2):
        s1, s2, ys = 0, 0, self.cols.y
        for col in ys:
            x = col.norm(row1[col.at])
            y = col.norm(row2[col.at])
            s1 = s1 - math.exp(col.w * (x - y) / len(ys))
            s2 = s2 - math.exp(col.w * (y - x) / len(ys))
        return s1/len(ys) < s2/len(ys)

    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(self.cols.x or cols):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** 2
        return (d / n) ** (1 / 2)

    def clone(self, init=[]):
        data = DATA(self.cols.names)
        _ = list(map(data.add, init))
        return data
