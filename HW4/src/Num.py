import math

class NUM():
  def __init__(self, at=0, txt=None):
    s = "NUM"
    self.n = 0
    self.mu = 0
    self.m2 = 0
    self.lo = float('inf')
    self.hi = float('-inf')
    if txt:
        self.txt = txt
    else:
        self.txt = ""
    self.w = -1 if self.txt.find("-$") != -1 else 1
    self.at = at

  def add(self, n):
    if n != "?":
      self.n += 1
      n = float(n)
      d = n - self.mu
      self.mu = self.mu + d/(self.n)
      self.m2 += d*(n - self.mu)
      self.lo = min(n, self.lo)
      self.hi = max(n, self.hi)

  def mid(self):   # removing x as not used
    return self.mu

  def div(self):
    return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5

  def rnd(self, x, n):
    if x == "?":
      return x
    else:
      return round(x, n)
  
  def norm(self, n):
    return n if n == "?" else (float(n) - self.lo) / (self.hi - self.lo + 1 + 10 ** (-32))

  

  def dist(self, n1, n2):
    if n1 == "?" and n2 == "?":
      return 1
    n1, n2 = self.norm(n1), self.norm(n2)
    if n1 == "?":
      n1 = 1 if n2 < 0.5 else 0
    if n2 == "?":
      n2 = 1 if n1 < 0.5 else 0
    return abs(n1 - n2)
