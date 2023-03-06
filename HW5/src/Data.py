from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from operator import itemgetter
from collections.abc import Iterable
import random
import re
from src.str_util import *
from src.Cols import COLS
from src.query import *
from src.helpdict import *

##update funtions
def row(data, t):
    # print("In row")
    # print(t)
    if data["cols"]:
        data["rows"].append(t)
        for cols in [data["cols"]["x"], data["cols"]["y"]]:
        
            for col in cols:
                
                
                # print(t)
                # if col!=6:
                add(col, t[col['at']])
    else:
        data["cols"]= COLS(t)
    return data


# def row(data, t):
#     if data.cols:
#         data.rows.append(t)
#         for cols in [data.cols.x, data.cols.y]:
#             for col in cols:
#                 add(col.col, t[col.col.at])
#     else:
#         data.cols = COLS(t)
#     return


def rand(lo=0, hi=1):
  Seed = 93716211
  lo = lo or 0
  hi = hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647


def rint(lo=0, hi=1):
  return math.floor(0.5 + rand(lo, hi))


def add(col, x, n = 1):
    if x != '?':
        n = n or 1
        col['n'] += n
        if col.isSym:
            col['has'][x] = n + col['has'].get(x, 0)
            if col['has'][x] > col['most']:
                col['most'], col['mode'] = col['has'][x], x
        else:
            col['lo'] = min(x, col['lo'])
            col['hi'] = max(x, col['hi'])
            all_ = len(col['has'])
            pos = (all_ < 512 and all_+1) or (rand()< 512/col['n'] and rint(1, all_))
            if pos:
                
                col['has'][pos-1] = x
                col['ok'] = False
    # if x != "?":
    #     col.n = col.n + n # Source of variable 'n'
    #     if hasattr(col, "isSym"):
    #         col.has[x] = n + (col.has.get(x, 0))
    #         print("ahuahucauau---------", col.has[x])
    #         print(col.most)
    #         if col.has[x] > col.most:
    #             col.most = col.has[x]
    #             col.mode = x
    #     else:
    #         col.lo = min(x, col.lo)
    #         col.hi = max(x, col.hi)
    #         all = len(col.has)
    #         if all < 512:
    #             pos = all + 1
    #         elif random.random() < 512 / col.n:
    #             pos = rint(1, all)
    #         else:
    #             pos = None
    #         if pos:
    #             if isinstance(col.has, dict):
    #                 col.has[pos] = x
    #             else:
    #                 col.has.append(x)
    #             col.ok = False

def adds(col, t):
    for value in t or []:
        add(col, value)
    return col

def extend(range, n, s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    add(range['y'], s)

#end of update function




def cells(s):
    t = []
    for s1 in re.findall("[^,]+", s):
        t.append(coerce(s1))
    return t

def lines(sFilename, fun):
    with open(sFilename, "r") as src:
        for s in src:
            s = s.rstrip("\r\n")
            fun(s)
    src.close()

def CSV(sFilename, fun):
    lines(sFilename, lambda line: fun(cells(line)))


## data functions!!
def new():
    return {"rows":[], "cols":None}

def read(sFile):
    data = new()
    callback = lambda t: row(data, t)
    CSV(sFile, callback)
    return data

def clone(data, ts = None, data1 = None):
    # print(data)
    data1 = row(new(), data["cols"]["names"])
    # print("ts", ts)
    for t in (ts or []):
        # print(t)
        row(data1, t)
    return data1


# class DATA:
   
#     def __init__(self, src):
#         self.rows = []
#         self.cols = None
#         # self.halfCalls = 0
#         fun = lambda x: self.add(x)
#         if type(src) == str:
#             self.csv(src)
#         else:
#             for row in src:
#                 self.add(row)
        
    # def add(self, t):
    #     if self.cols:
    #         t = t if hasattr(t, "cells") else ROW(t)
    #         self.rows.append(t)
    #         self.cols.add(t)
    #     else:
    #         self.cols = COLS(t)

    # def csv(self, file: str):
    #     with open(file, "r") as csv:
    #         lines = csv.readlines()
    #         for line in lines:
    #             split_line = line.replace("\n", "").rstrip().split(",")
    #             split_line = [coerce(i) for i in split_line]
    #             self.add(split_line)
    #             self.n += len(split_line)

    # def stats(self, what, cols, n_places):
    #     def fun(k, col):
    #         callable = getattr(col, what)
    #         return col.rnd(callable(), n_places), col.txt

    #     return kap(cols, fun)

    # # def better(self, row1, row2):
    # #     s1, s2, ys = 0, 0, self.cols.y
    # #     for col in ys:
    # #         x = col.norm(row1[col.at])
    # #         y = col.norm(row2[col.at])
    # #         s1 = s1 - math.exp(col.w * (x - y) / len(ys))
    # #         s2 = s2 - math.exp(col.w * (y - x) / len(ys))
    # #     return s1 / len(ys) < s2 / len(ys)

    # def dist(self, row1, row2, cols=None):
    #     n, d = 0, 0
    #     for _, col in enumerate(self.cols.x or cols):
    #         n = n + 1
    #         d = d + col.dist(row1.cells[col.at], row2.cells[col.at]) ** 2
    #     return (d / n) ** (1 / 2)

    # def clone(self, rows=None):
    #     data = DATA([self.cols.names])
    #     for row in rows:
    #         data.add(row)
    #     return data
    # # def sway(self, rows=None, min=None, cols=None, above=None):
    # #     rows = rows or self.rows
    # #     min = min or len(rows) ** 0.5
    # #     cols = cols or self.cols.x
    # #     node = {"data": self.clone(rows)}
    # #     if len(rows) > 2 * min:
    # #         left, right, node["A"], node["B"], node["min"], _ = self.half(
    # #             rows, cols, above
    # #         )
    # #         if self.better(node["B"], node["A"]):
    # #             left, right, node["A"], node["B"] = right, left, node["B"], node["A"]
    # #         node["left"] = self.sway(left, min, cols, node["A"])
    # #     if "left" not in node:
    # #         node["left"] = None
    # #     if "right" not in node:
    # #         node["right"] = None
    # #     return node

    # def around(self, row1, rows=None, cols=None):
    #     if rows is None:
    #         rows = self.rows
    #     if isinstance(rows, Iterable):
    #         iterable = rows
    #     else:
    #         iterable = self.rows
    #     rows_with_distance = [(row2, self.dist(row1, row2, cols))
    #                           for row2 in iterable]
    #     sorted_rows = sorted(rows_with_distance, key=lambda x: x[1])
    #     return [(row, dist) for row, dist in sorted_rows]

    # def cluster(self, rows=None, cols=None, above=None):
    #     rows = rows if rows else self.rows
    #     cols = cols if cols else self.cols.x
    #     node = {"data": self.clone(rows)}
        
    #     if len(rows) >= 2:
    #         left, right, node["A"], node["B"], node["mid"], node["C"] = self.half(rows, cols, above)
    #         node["left"] = self.cluster(left, cols, node["A"])
    #         node["right"] = self.cluster(right, cols, node["B"])
    #     return node
        
    # def furthest(self, row1, rows, cols=None):
    #     t = self.around(row1, rows, cols)        
    #     return t[-1][0]

    # def half(self, rows=None, cols=None, above=None):
    #     A, B, left, right, c, mid, some = None, None, None, None, None, None, None
    #     def any(t):
    #         rintVal = rint1(None, len(t)-1)
    #         return t[rintVal]
    #     def rint1(lo, hi):
    #         return math.floor(0.5 + rand1(lo, hi))
    #     def rand1(lo, hi):
    #         Seed =  93716211
    #         lo = lo or 0
    #         hi = hi or 1
    #         Seed = (16807 * Seed) % 2147483647
    #         return lo + (hi - lo) * Seed / 2147483647
            
    #     def cosine(a, b, c):
    #         den = 1 if c == 0 else 2 * c
    #         x1 = (a**2 + c**2 - b**2) / den
    #         x2 = max(0, min(1, x1))
    #         y = abs((a**2 - x2**2)) ** 0.5
    #         return x2, y
    #     def project(row):
    #         x, y  = cosine(dist2(row, A), dist2(row, B), c)
    #         row.x = x or row.x
    #         row.y = y or row.y
    #         return {'row': row, 'x': x, 'y': y}
    #     def dist2(row1, row2, cols=None):         
    #         return self.dist(row1, row2, cols)
    #     rows = rows or self.rows
    #     A = any(rows)
    #     B = self.furthest(A, rows)
    #     c = dist2(A, B)
    #     left, right = [], []
    #     mapVAR = [project(row) for row in rows]
    #     sorted_rows = sorted(mapVAR, key=lambda x: x["x"])
    #     for n, tmp in enumerate(sorted_rows):
    #         if n <= len(rows) // 2 - 1:
    #             left.append(tmp["row"])
    #             mid = tmp["row"]
    #         else:
    #             right.append(tmp["row"])
    #     return left, right, A, B, mid, c


    
   
