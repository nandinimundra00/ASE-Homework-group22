# Misc functions:
import csv
from csv import reader
from src.Misc import *
import math
import sys
import re
import os

def fmt(sControl, *args):
  return sControl.format(*args)

def o(t):
  if (type(t) !=  dict and type(t).__module__ == "__builtin__"):
    return str(t)
  if(type(t).__module__ != "__builtin__" and type(t) != dict):
    newDictionary = (vars(t))
    newDictionary.pop('_has')
    return newDictionary

  print(t)
  def show(k,v):
    first = k[0]
    if(str(first)!="_"):
      if(type(v) == dict):
        v = o(v)
        if(len(t) == 0):
          return ":"+str(k)+str(v)
        else:
          return str(v)
  u={}
  for k,v in t.items():
    u_len = len(u)
    u[k] = show(k,v)
  if len(t)==0:
    u = sorted(u)
  output = ""
  for key in u:
    output = output + ":" + key + " " + str(u[key]) + " "
  return "{" + output + "}"
  
def oo(t):
  print(o(t))
  return t 

def coerce(s: str):
    def fun(s1: str):
        if s1 == 'true' or s1.lower() == 'true':
            return True
        if s1 == 'false' or s1.lower() == 'false':
            return False
        return s1
    val = s
    try:
        val = float(s)
        if val == int(val):
            val = int(val)
    except ValueError:
        val = fun(re.search('^\s*(.+?)\s*$', s).group(1))
    return val

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
