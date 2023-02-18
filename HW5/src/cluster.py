import math
from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from src.query import *
from src.Data import *


def half(data, rows = None, cols = None, above = None):
    left = []
    right = []
    def gap(r1, r2):
        return dist(data, r1, r2, cols)
    
    def cos(a, b, c):
        return (a**2 + c**2 - b**2)/(2*c)

    def proj(r):
        return {'row': r, 'x': cos(gap(r, A), gap(r, B), c)}
    
    rows = rows or data.rows
    some = many(rows, 512)
    A = above if True else any(some)
    tmp = sorted([{"row": r, "d": gap(r, A)} for r in some], key=lambda x: x["d"])
    far = tmp[int(len(tmp)*0.95)]
    B, c = far["row"], far["d"]
    sorted_rows = sorted(map(rows, proj), key=lambda x: x["x"])
    left, right = [], []
    for n, two in enumerate(sorted_rows):
        if n <= (len(rows) - 1) / 2:
            left.append(two["row"])
        else:
            right.append(two["row"])
    return left, right, A, B, c


def tree(data, cols, above, rows = None):
    rows = rows
    here = {"data" : clone(data, rows)}
    if len(rows)>=2*(len(data.rows)**0.5):
        left,right,A,B = half(data, rows, cols, above)
        here["left"] = tree(data, left, cols, A)
        here["right"] = tree(data, right, cols, B)
    return here

def showTree(tree, lvl = 0, post = None):
    if tree:
        print("{}[{}]".format("|.. " * lvl, len(tree.data.rows)), end="")
        if lvl == 0 or not tree.left:
            print(stats(tree.data))
        else:
            print("")
        showTree(tree.left, lvl + 1)
        showTree(tree.right, lvl + 1)



######## Optimization #######
def sway(data):
    def worker(rows, worse, above = None):
        if len(rows) <= len(data.rows)**0.5:
            return rows, many(worse, 4*len(rows))
        else:
            l , r, A, B, dummy = half(data, rows, None, above)
            if better(data, B, A):
                l, r, A, B = r, l, B, A
            map(r, lambda row: worse.append(row))
            return worker(l, worse, A)
    best, rest = worker(data.rows, [])
    return clone(data, best), clone(data, rest)

