from src.add import *
class NUM():
  def __init__(self, t = []):
    self.n = 0
    self.mu = 0
    self.m2 = 0
    self.sd = 0
    for x in t:
      add(self, x)

