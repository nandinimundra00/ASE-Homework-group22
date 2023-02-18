import math
from copy import deepcopy
from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from src.query import *
from src.Data import *
from src.cluster import *

def itself(x):
    return x

def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = []
        for y, rows in enumerate(rowss):
            for row in rows:
                x = row[col.at]
                if x != "?":
                    k = bin(col, x)
                    ranges[k] = ranges[k] or RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
        ranges = sorted(map(ranges, itself))
        if col.isSym:
            out.append(ranges)
        else:
            out.append(mergeAny(ranges))
    return out

def bin(col, x):
    if x=="?" or col.isSym:
        return x
    tmp = (col.hi - col.lo)/(16 - 1)
    return 1 if col.hi == col.lo else math.floor(x/tmp + 0.5)*tmp

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)):
            t[j].lo = t[j-1].hi
        t[0].lo = -math.huge
        t[-1].hi = math.huge
        return t
    ranges1 = []
    j = 0
    while j<= ranges0:
        left, right = ranges0[j], ranges0[j+1]
        if right:
            y = merge2(left.y, right.y)
            if y:
               j = j+1
               left.hi = right.hi
               left.y = y 
        ranges1.append(left)
        j += 1
    if len(ranges1)==len(ranges0):
        return noGaps(ranges0)
    else:
        return  mergeAny(ranges1)

def merge2(col1, col2):
    new = merge(col1, col2)
    if div(new) <= (div(col1)*col1.n + div(col2)*col2.n)/new.n:
        return new

def merge(col1, col2):
    new = deepcopy(col1)
    if col1.isSym:
        for x, n in enumerate(col2.has):
            add(new, x, n)
    else:
        for n in col2.has:
            add(new, n)
        new.lo = min(col1.lo, col2.lo)
        new.hi = max(col1.hi, col2.hi)
    return new

