# Misc functions:
from typing import Any, cast
import csv
from csv import reader
from src.str_util import *
from src.Misc import *
import math
import sys
import re
import os
import io
import random

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

def CSV(fname, fun):
  sep = "([^" + "\," + "]+"
  with open(fname) as file_obj:
    reader_obj = reader(file_obj)
    for row in reader_obj:
      t = {}
      for element in row:
        t[str(1 + len(t))] = coerce(element)
      fun(t)



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



def show(node, what, cols, n_places, lvl=0):
    if node:
        lvl = lvl or 0
        print("| " * lvl, str(len(node["data"].rows)), " ")
        if not node.get("left", None) or lvl == 0:
            print(o(node["data"].stats("mid", node["data"].cols.y, n_places)))
        else:
            print("")
        show(node.get("left", None), what, cols, n_places, lvl + 1)
        show(node.get("right", None), what, cols, n_places, lvl + 1)


