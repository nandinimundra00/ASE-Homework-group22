#SYM Class
import math


class SYM():
  def __init__(self, at=None, txt=None):
    s = "SYM"
    self.n = 0
    self.has = {}
    self.mode = None
    self.most = 0
    if at:
        self.at = at
    else:
        self.at = 0
    if txt:
        self.txt = txt
    else:
        self.txt = ""

  def mid(self):
    return self.mode

  def add(self, x):
    if x != "?":
      self.n += 1
      # can modify this!!
      self.has[x] = 1 + (self.has[x] if x in self.has else 0)
      if self.has[x] > self.most:
        self.most = self.has[x]
        self.mode = x

  def div(self):
    def fun(p):
      return p*math.log(p, 2)
    e = 0
    for k, v in self.has.items():
      e += fun(v/self.n)
    return -e

  def rnd(n):
    return n

  def dist(self, s1, s2):
    if s1 == "?" and s2 == "?":
      return 1
    elif s1 == s2:
      return 0
    else:
      return 1
