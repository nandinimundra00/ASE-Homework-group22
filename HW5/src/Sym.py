#SYM Class
import math


class SYM():
    def __init__(self, n = 0, s = ""):
        self.at = n
        self.txt = s
        self.n = 0
        self.isSym = True
        self.has = {}
        self.most = 0
        self.mode = None
       

#   def add(self, x):
#       if x != "?":
#           self.n += 1
#           self.has[x] = 1 + self.has.get(x, 0)  # Return to later for dictionary
#           if self.has[x] > self.most:
#               self.most = self.has[x]
#               self.mode = x

#   def mid(self):
#       return self.mode

#   def div(self):
#       def fun(p):
#           return p * math.log(p, 2)

#       e = 0
#       for _, value in self.has.items():
#           e += fun(value / self.n)
#       return -e
  
#   def dist(self, s1, s2):
#       return 1 if (s1 == "?" and s2 == "?") else 0 if (s1 == s2) else 1

#   def rnd(self, x, n):
#       return x