from typing import Any, cast
import csv
from csv import reader
from src.Data import *
from src.str_util import *
import math
import sys
import re
import os
import io
import random
from copy import deepcopy
from src.consts import *
global Seed


def settings(s):
  t = {}
  for k, v in re.findall('\n [\s]+[-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', s):
    t[k] = coerce(v)
   
  return t

def cli(options):
    args = sys.argv
    for k, v in options.items():
        v = str(v)
        for i in range(1, len(args)):
            if args[i] == '-' + k[0:1] or args[i] == '--' + k:
              if v == "False":
                v = "true"
              elif v == "True":
                v = "false"
              else:
                v = args[i + 1]
        options[k] = coerce(v)
    return options



def rand(lo=0, hi=1):
  Seed =  93716211
  lo = lo or 0
  hi = hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647


def rint(lo=0, hi=1):
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces=2):
  x = nPlaces or 2
  mult = 10**x
  return math.floor(n * mult + 0.5) / mult

def push(t, x):
    t.append(x)
    # t[1+len(t)] = x
    return x

def cosine(a, b, c):
    den = 1 if c == 0 else 2 * c
    x1 = (a**2 + c**2 - b**2) / den
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2)) ** 0.5
    return x2, y

def any(t):
  rintVal = rint(None, len(t)-1)
  return t[rintVal]

def many(t, n):
  return [any(t) for i in range(n)]
  
def show(node, what=None, cols=None, n_places=None, lvl=None):
    if node:
      lvl = lvl or 0
      print("|.. " * lvl, end="")
      if ("left" not in node):
          print(last(last(node["data"].rows).cells))
      else:
          print(str(int(100 * node["C"])))
      show(node.get("left", None), what, cols, n_places, lvl+1)
      show(node.get("right", None), what, cols, n_places, lvl+1)


def last(t):
    return t[-1]


def transpose(t):
  u = []
  for i in range(len(t[0])):
      u.append([t[j][i] for j in range(len(t))])
  return u

def repCols(cols):
    copyCols = deepcopy(cols)
    for col in cols:
        col[-1] = str(col[0]) + ":" + str(col[-1])
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    cols.insert(0, ['Num' + str(k) for k in range(len(cols[0]))])
    cols[0][-1] = "thingX" 
    return DATA(cols)

def repRows(t,rows, u=None):
  rows = deepcopy(rows)
  for j, s in enumerate(rows[-1]):
    rows[0][j] = str(rows[0][j]) + ":" + str(s)
  rows.pop()
  for n, row in enumerate(rows):
    if n==0:
      row.append("thingX")
    else:
      u = t["rows"][len(t["rows"]) - n]
      row.append(u[-1])
  return DATA(rows)
  
def repPlace(data):
  n,g = 20,[]
  for i in range(n+1):
      g.append([])
      for j in range(n+1):
          g[i].append(" ")
  maxy = 0
  print("")
  for r, row in enumerate(data.rows):
      c = chr(r+65)
      print(c, last(row.cells))
      x, y = int(row.x*n), int(row.y*n)
      maxy = max(maxy, y)
      g[y][x] = c
  print("")
  for y in range(maxy):
      print("{" + "".join(g[y]) + "}")

def repgrid(sFile, t, rows, cols):
  t = exec(open(sFile).read())
  rows = repRows(t, transpose(t["cols"]))
  cols = repCols(t["cols"])
  show(rows.cluster())
  show(cols.cluster())
  repPlace(rows)


def itself(x):
  return x


def cliffsDelta(ns1, ns2):
    if len(ns1) > 256:
        ns1 = many(ns1, 256)
    if len(ns2) > 256:
        ns2 = many(ns2, 256)
    if len(ns1) > 10 * len(ns2):
        ns1 = many(ns1, 10 * len(ns2))
    if len(ns2) > 10 * len(ns1):
        ns2 = many(ns2, 10 * len(ns1))
    n, gt, lt = 0, 0, 0
    for _, x in enumerate(ns1):
        for _, y in enumerate(ns2):
            n += 1
            if x > y:
                gt += 1
            if x < y:
                lt += 1
    return abs(lt - gt)/n > 0.147

def diffs(nums1, nums2):
    def kap(nums1, func):
        return [func(k, nums) for k, nums in enumerate(nums1)]

    return kap(nums1, lambda k, nums: (cliffsDelta(nums["has"], nums2[k]["has"]), nums["txt"]))
