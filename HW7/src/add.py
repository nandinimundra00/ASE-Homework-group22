import math
def add(i, x):
    i.n += 1
    d = x - i.mu
    i.mu = i.mu + d/i.n
    i.m2 = i.m2 + (d*(x - i.mu))
    i.sd = 0  if i.n<2 else math.sqrt(i.m2 / (i.n - 1))
