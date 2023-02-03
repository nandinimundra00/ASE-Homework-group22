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
