from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from operator import itemgetter

class DATA:
   
    
    def __init__(self, src):
        self.rows = []
        self.cols = None
        # self.halfCalls = 0
        fun = lambda x: self.add(x)
        if type(src) == str:
            self.csv(src)
        else:
            for row in src:
                self.add(row)

    def add(self, t):
        """
        Function:
            add
        Description:
            Adds the data to rows and cols, or makes a COLS if there aren't any columns stored yet
        Input:
            self - current DATA instance
            t - data to be added
        Output:
            None
        """
        if self.cols:
            t = t if hasattr(t, "cells") else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def csv(self, file: str):
        with open(file, "r") as csv:
            lines = csv.readlines()
            for line in lines:
                split_line = line.replace("\n", "").rstrip().split(",")
                split_line = [coerce(i) for i in split_line]
                self.add(split_line)
                self.n += len(split_line)

    def stats(self, what, cols, n_places):
        def fun(k, col):
            callable = getattr(col, what)
            return col.rnd(callable(), n_places), col.txt

        return kap(cols, fun)

    # def better(self, row1, row2):
    #     s1, s2, ys = 0, 0, self.cols.y
    #     for col in ys:
    #         x = col.norm(row1[col.at])
    #         y = col.norm(row2[col.at])
    #         s1 = s1 - math.exp(col.w * (x - y) / len(ys))
    #         s2 = s2 - math.exp(col.w * (y - x) / len(ys))
    #     return s1 / len(ys) < s2 / len(ys)

    def dist(self, row1, row2, cols=None):
        n, d = 0, 0
        for _, col in enumerate(self.cols.x or cols):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** 2
        return (d / n) ** (1 / 2)

    def clone(self, init=None):
        if init is None:
            init = []
        data = DATA(self.cols.names)
        _ = list(map(data.add, init))
        return data

    # def sway(self, rows=None, min=None, cols=None, above=None):
    #     rows = rows or self.rows
    #     min = min or len(rows) ** 0.5
    #     cols = cols or self.cols.x
    #     node = {"data": self.clone(rows)}

    #     if len(rows) > 2 * min:
    #         left, right, node["A"], node["B"], node["min"], _ = self.half(
    #             rows, cols, above
    #         )
    #         if self.better(node["B"], node["A"]):
    #             left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
    #         node["left"] = self.sway(left, min, cols, node["A"])
    #     if "left" not in node:
    #         node["left"] = None
    #     if "right" not in node:
    #         node["right"] = None
    #     return node

    def around(self, row1, rows=None, cols=None):
        if rows is None:
            rows = self.rows

        def distance(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}

        sorted_rows = sorted(map(distance, rows), key=lambda x: x["dist"])
        return sorted_rows

    def cluster(self, rows=None, cols=None, above=None):
        
        rows = rows or self.rows
        cols = cols or self.cols.x
        node = {"data": self.clone(rows)}

        if len(rows) >= 2 :
            left, right, node["A"], node["B"], node["min"], node["c"] = self.half(rows, cols, above)
            node["left"] = self.cluster(left, cols, node["A"])
            node["right"] = self.cluster(right, cols, node["B"])
            
        return node
        
    def furthest(self, row1, rows, cols):
        t = self.around(row1, rows, cols)
        return t[len(t)]


    def half(self, rows=None, cols=None, above=None):
        def distD(row1, row2):
            return self.dist(row1, row2, cols)

        def project(row):
            x,y = cosine(distD(row, A), distD(row, B), c)
            row.x = row.x or x
            row.y = row.y or y
            return {
                "row": row,
                "x": x,
                "y": y
            }

        if rows is None:
            rows = self.rows

        A = above or any(rows)
        B = self.furthest(A, rows)["row"]
        c = distD(A, B)
        left, right, mid = [], [], None
        for n, tmp in enumerate(
            sorted(list(map(project, rows)), key=lambda x: x["x"])
        ):
            if n <= len(rows) / 2:
                left.append(tmp["row"])
                mid = tmp["row"]
            else:
                right.append(tmp["row"])
        return left, right, A, B, mid, c

    

