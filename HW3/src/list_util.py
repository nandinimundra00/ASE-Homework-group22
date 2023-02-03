def kap(t, fun):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        u[k or (1 + len(u))] = v
    return u

def sort(t, fun):
  t = sorted(t, key = fun)
  return t

def keys(t):
  def temp(k):
    return k
  return sort(kap(t, temp))

def lt(x):
  def sort_func(a, b):
    return a[x] < b[x]
  return sort_func
