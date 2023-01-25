#List functions 
def map(t, fun, u = {}):
  for k, v in t.items():
    print(fun(v))
    v, k = fun(v)
    temp = k if k else (1 + len(u))
    u[temp] = v
  return u

def kap(t, fun, u = {}):
  for k, v in t.items():
    v, k = fun(k, v)
    temp = k if k else (1 + len(u))
    u[temp] = v
  return u
