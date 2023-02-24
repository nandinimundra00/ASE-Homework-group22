import math
from src.Misc import *
def kap(t, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or (1 + len(u))] = v
    return u

def sort(t, fun):
  t = sorted(t, key = fun)
  return t

def keys(t):
  def temp(k):
    return k
  return sort(kap(t, temp))

def lt(x):
  def sort_func(a, b):
    return a[x] < b[x]
  return sort_func

def push(t, x):
  t.append(x)
  return x
    # t[1+len(t)] = x
    # return x


def any(t):
  rintVal = rint(None, len(t)-1)
  return t[rintVal]


def many(t, n):
  return [any(t) for i in range(n)]


def at(x):
    return lambda t: t[x]


def lt(x):
  return lambda a,b: a[x] < b[x]


def gt(x):
  return lambda a, b: a[x] > b[x]


def per(t, p=0.5):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(0, min(len(t), p - 1))]


def copy(t):
    if type(t) != "table":
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u


def slice(t, go=1, stop=None, inc=1):
    if go and go < 0:
        go = len(t) + go
    if stop and stop < 0:
        stop = len(t) + stop
    u = []
    for j in range((go or 1) - 1, (stop or len(t)), inc):
        u.append(t[j])
    return u

def rint(lo=0, hi=1):
  return math.floor(0.5 + rand(lo, hi))


def rand(lo=0, hi=1):
  Seed =  93716211
  lo = lo or 0
  hi = hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647