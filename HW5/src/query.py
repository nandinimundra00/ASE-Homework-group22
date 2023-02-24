import math
from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *


def has(col):
    if not col.isSym and not col.ok:
        sorted(col['has'])
    col['ok'] = True
    return col['has']
    # if not col.ok and not hasattr(col, "isSym"):
    #      if isinstance(col.has, dict):
    #         col.has = dict(sorted(col.has.items(), key = lambda item: item[1]))
    # else:
    #     col.has.sort()
    # col.ok = True
    # return col.has
    # if hasattr(col, "isSym"):
    #     return True
    
    # else:
    #     col['has'].sort()
    #     col['ok'] = True
    # print(col)
    # return col

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p)) - 1]
    # p = math.floor(((p or 0.5) * len(t)) + 0.5)
    # return t[max(1, min(len(t), p))]

def mid(col):
    
    return col.mode if col.isSym else per(has(col), 0.5)


def stats(data, nPlaces=2, fun = None, cols = None):
    # cols = cols or data["cols"]["y"]
    # def fun(k, col):
    #     return round((fun or mid)(col), nPlaces), col["txt"]
    # tmp = kap(cols, fun)
    # tmp["N"] = len(data["rows"])
    # return tmp, map(cols, mid)
    # cols = cols or data["cols"]["y"]
    # tmp = {}
    # for k, col in enumerate(cols):
    #     val = (fun or mid)(col)
    #     if nPlaces is not None:
    #         val = round(val, nPlaces)
    #     tmp[col.txt] = val
    # tmp["N"] = len(data["rows"])
    # return tmp, [mid(col) for col in cols]
    cols = cols or data["cols"]["y"]
    print("--------------")
    # print(data)
    def callBack(k, col):
        # print("Col:", col)
        col = col
        return round((fun or mid)(col), nPlaces), col["txt"]
    tmp = kap(cols, callBack)
    tmp["N"] = len(data["rows"])
    return tmp, map(mid, cols)

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

def value(has, nB = 1 , nR = 1, sGoal = True):
    b, r = 0, 0
    for x, n in has.items():
        if x == sGoal:
            b = b + n
        else:
            r = r + n
    b,r = b/(nB+1/float("inf")), r/(nR+1/float("inf"))
    return (b ** 2) / (b + r)

def dist(data, t1, t2, cols = None):
    def dist1(col, x, y):
        if x == "?" and y == "?":
            return 1
        if col.isSym:
            return 0 if x == y else 1
        x, y = norm(col, x), norm(col, y)
        if x == "?":
            x = 1 if y < 0.5 else 1
        if y == "?":
            y = 1 if x < 0.5 else 1
        return abs(x - y)
    d = 0
    n = 1 / float("inf")
    cols = cols or data['cols']['x']
    for col in cols:
        n = n + 1
        d = d + dist1(col, t1[col['at']], t2[col['at']])**2
    return (d / n)**(1 / 2)

def better(data, row1, row2):
    s1 = 0
    s2 = 0
    ys = data["cols"]["y"]
    for _, col in enumerate(ys):
        x = norm(col, row1[col.at])
        y = norm(col, row2[col.at])

        s1 = s1 - math.exp(col.w * (x-y)/len(ys))
        s2 = s2 - math.exp(col.w * (y - x)/len(ys))

    return s1/len(ys) < s2 / len(ys)
