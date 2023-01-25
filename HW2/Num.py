class NUM():
  def __init__(self, at=0, txt=""):
    s = "NUM"
    self.n = 0
    self.mu = 0
    self.m2 = 0
    self.lo = float('inf')
    self.hi = float('-inf')
    self.at = at
    self.txt = txt
    if self.txt == "":
      self.w=1
    else:
      if self.txt[-1] == '-':
        self.w = -1
      else:
        self.w = 1

  def add(self, n):
    if n != "?":
      self.n += 1
      d = n - self.mu
      self.mu = self.mu + d/(self.n)
      self.m2 += d*(n - self.mu)
      self.lo = min(n, self.lo)
      self.hi = max(n, self.hi)

  def mid(self):   # removing x as not used
    return self.mu

  def div(self):
    if (self.m2 < 0 or self.n < 2):
      return 0
    else:
      return (self.m2/(self.n - 1))**0.5

  def rnd(x, n):
    if x == "?":
      return x
    else:
      return round(x, n)
