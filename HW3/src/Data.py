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

    def sway(self, rows=None, min=None, cols=None, above=None):
        rows = rows or self.rows
        min = min or len(rows) ** 0.5
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) > 2 * min:
            left, right, node["A"], node["B"], node["min"], _ = self.half(rows, cols, above)
            
            if self.better(node["B"], node["A"]):
                left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
           
            node["left"] = self.sway(left, min, cols, node["A"])
        
        if "left" not in node:
            node["left"] = None
        if "right" not in node:
            node["right"] = None
        return node

    def around(self, row1, rows=None, cols=None):
        if rows is None:
            rows = self.rows

        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        row_sorted = sorted(map(distance, rows), key=lambda x: x["dist"])
        return row_sorted

    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        if rows is None:
            rows = self.rows
        min_size = min_size or (len(rows)) ** 0.5
        if cols is None:
            cols = self.cols.x
        node = {"data": self.clone(rows)}  # xxx cloning
        if len(rows) > 2 * min_size:
            left, right, node["A"], node["B"], node["mid"], _ = self.half(
                rows, cols, above
            )
            node["left"] = self.cluster(left, min_size, cols, node["A"])
            node["right"] = self.cluster(right, min_size, cols, node["B"])
        if "left" not in node:
            node["left"] = None
        if "right" not in node:
            node["right"] = None
        return node
