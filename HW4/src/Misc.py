from typing import Any, cast
import csv
from csv import reader
from src.Data import DATA
from src.str_util import *
from src.Misc import *
import math
import sys
import re
import os
import io
import random
from copy import deepcopy

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

global Seed

def rand(lo, hi):
  Seed =  93716211
  lo = lo or 0
  hi = hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647

def rint(lo, hi):
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces):
  x = nPlaces or 3
  mult = 10**x
  return math.floor(n * mult + 0.5) / mult

def push(t, x):
    t[1+len(t)] = x
    return x

def cosine(a, b, c):
    den = 1 if c == 0 else 2 * c
    x1 = (a**2 + c**2 - b**2) / den
    x2 = max(0, min(1, x1))
    y = abs((a**2 - x2**2)) ** 0.5
    return x2, y

def any(t):
  return random.choice(t)

def many(t, n):
  return [any(t) for i in range(n)]

# ### might not work ####
# def copy(t):
#   if type(t) != dict:
#       return t
#   u = {}
#   for k, v in t.items():
#       u[copy(k)] = copy(v)
#   return u
     
  
def show(node, what=None, cols=None, n_places=None, lvl=None):
    # if node:
    #     lvl = lvl or 0
    #     print("| " * lvl, str(len(node["data"].rows)), " ")
    #     if not node.get("left", None) or lvl == 0:
    #         print(o(node["data"].stats("mid", node["data"].cols.y, n_places)))
    #     else:
    #         print("")
    #     show(node.get("left", None), what, cols, n_places, lvl + 1)
    #     show(node.get("right", None), what, cols, n_places, lvl + 1)
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
    print(t)
    return t[-1]


def transpose(t):
  u = {}
  for i in range(len(t)):
    u[i] = {}
    for j in range(len(t)):
      u[i][j] = t[j][i]
  return u

# def repCols(cols):
#   cols = deepcopy(cols)
#   print(cols, type(cols))
#   for col in cols:
#       col[-1] = col[0] + ":" + col[-1]
#       for j in range(1, len(col)):
#          col[j-1] = col[j]
#       col.pop()
#   cols.insert(0, {k: "Num" + str(k) for k in cols[0]})
#   cols[0][-1] = "thingX"
#   return DATA(cols)


def repCols(cols):
    copyCols = deepcopy(cols)
    for col in cols:
        col[-1] = str(col[0]) + ":" + str(col[-1])
        for j in range(1, len(col)):
            col[j - 1] = col[j]
        col.pop()
    cols.insert(0, ['Num' + str(k) for k in range(len(cols[0]))])
    cols[0][-1] = "thingX"
    
    print("___________")
    print(cols)
    
    return DATA(cols)

# function repRows(t, rows,u)
#   rows=copy(rows)
#   for j,s in pairs(rows[#rows]) do rows[1][j] = rows[1][j] .. ":" .. s end
#   rows[#rows] = nil
#   for n,row in pairs(rows) do
#     if n==1 then push(row,"thingX") else
#       u=t.rows[#t.rows - n + 2]
#       push(row, u[#u]) end end
#   return  DATA(rows) end

def repRows(t):
  rows = deepcopy(rows)
  for j, s in (rows[len(rows)]).items():
    rows[1][j] = rows[1][j] + ":" + s
  rows.pop()
  for n, row in rows.items():
    if(n == 1):
        push(row, "thingX")
    else:
        u=t.rows[len(t.rows) - n + 2]
        push(row, u[len(u)])
    return DATA(rows)
  
def repPlace(data):
  n, g = 20, {}
  for i in range(1, n+1):
      g[i] = {}
      for j in range(1, n+1):
         g[i][j]=" "
  print("")
  for r, row in data.rows.items():
    c = chr(64 + r)
    print(c, row.cells[-1])
    x, y = int(row.x * n), int(row.y * n)
    maxy = max(maxy, y + 1)
    g[y + 1][x + 1] = c
  print("")
  for y in range(1, maxy + 1):
     print("".join(g[y]))
  

def repgrid(sFile, t, rows, cols):
  t = exec(open(sFile).read())
  rows = repRows(t, transpose(t["cols"]))
  cols = repCols(t["cols"])
  show(rows.cluster())
  show(cols.cluster())
  repPlace(rows)






        


