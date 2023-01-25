import math

class SYM():
  def __init__(self):
    s = "SYM"
    self.n = 0
    self.has = {}
    self.mode = None
    self.most = 0
  
  def mid(self):
    return self.mode
  
  def add(self, x):
    if x != "?":
      self.n += 1
      self.has[x] = 1 + (self.has[x] if x in self.has else 0) #can modify this!!
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
