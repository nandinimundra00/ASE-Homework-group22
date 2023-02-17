import math
from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *


def has(col):
    if not col.ok and not hasattr(col, "isSym"):
         if isinstance(col.has, dict):
            col.has = dict(sorted(col.has.items(), key = lambda item: item[1]))
    else:
        col.has.sort()
    col.ok = True
    return col.has

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]

def mid(col):
    return col.mode if hasattr(col, "isSym") else per(has(col), 0.5)


def stats(data, nPlaces, fun = None, cols = None):
    cols = cols or data.cols.y
    def fun(k, col):
        return round((fun or mid)(col), nPlaces), col.txt
    tmp = kap(cols, fun)
    tmp["N"] = len(data.rows)
    return tmp, map(cols, mid)

def div(col):
    if hasattr(col, "isSym"):
        e = 0
        if isinstance(col.has, dict):
            for n in col.has.values():
                e = e - n/col.n * math.log(n/col.n, 2)
        else:
            for n in col.has:
                e = e - n/col.n * math.log(n/col.n, 2)
        return e
    else:
        return (per(has(col),.9) - per(has(col), .1))/2.58

def norm(num, n):
    return n if n == "?" else (n - num.lo) / (num.hi - num.lo + 1 / float("inf"))
