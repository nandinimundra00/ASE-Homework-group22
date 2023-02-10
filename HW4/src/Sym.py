#SYM Class
import math


class SYM():
  def __init__(self, at=0, txt=""):
        self.at = at
        self.txt = txt
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

  def add(self, x):
      """
      Function:
          add
      Description:
          If n is not ?, n on the instance object is incremented by one and NUM attributes are re-calculated
      Input:
          self - current SYM instance
          n - value to add
      Output:
          None
      """
      if x != "?":
          self.n += 1
          self.has[x] = 1 + self.has.get(x, 0)  # Return to later for dictionary
          if self.has[x] > self.most:
              self.most = self.has[x]
              self.mode = x

  def mid(self):
      """
      Function:
          mid
      Description:
          returns the mode of the current instance
      Input:
          self - current SYM instance
      Output:
          mode
      """
      return self.mode

  def div(self):
      """
      Function:
          div
      Description:
          Determines if there is diversity around the center
      Input:
          self - current NUM instance
      Output:
          Diversity around the center
      """
      def fun(p):
          return p * math.log(p, 2)

      e = 0
      for _, value in self.has.items():
          e += fun(value / self.n)
      return -e
  
  def dist(self, s1, s2):
      return 1 if (s1 == "?" and s2 == "?") else 0 if (s1 == s2) else 1
    
    
  # def __init__(self, at=None, txt=None):
  #   s = "SYM"
  #   self.n = 0
  #   self.has = {}
  #   self.mode = None
  #   self.most = 0
  #   if at:
  #       self.at = at
  #   else:
  #       self.at = 0
  #   if txt:
  #       self.txt = txt
  #   else:
  #       self.txt = ""

  # def mid(self):
  #   return self.mode

  # def add(self, x):
  #   if x != "?":
  #     self.n += 1
  #     # can modify this!!
  #     self.has[x] = 1 + (self.has[x] if x in self.has else 0)
  #     if self.has[x] > self.most:
  #       self.most = self.has[x]
  #       self.mode = x

  # def div(self):
  #   def fun(p):
  #     return p*math.log(p, 2)
  #   e = 0
  #   for k, v in self.has.items():
  #     e += fun(v/self.n)
  #   return -e

  # def rnd(n):
  #   return n

  # def dist(self, s1, s2):
  #   if s1 == "?" and s2 == "?":
  #     return 1
  #   elif s1 == s2:
  #     return 0
  #   else:
  #     return 1
  
