import re

def fmt(sControl, *args):
  return sControl.format(*args)

def o(t):
  if (type(t) !=  dict and type(t).__module__ == "__builtin__"):
    return str(t)
  if(type(t).__module__ != "__builtin__" and type(t) != dict):
    newDictionary = (vars(t))
    newDictionary.pop('_has')
    return newDictionary

  print(t)
  def show(k,v):
    first = k[0]
    if(str(first)!="_"):
      if(type(v) == dict):
        v = o(v)
        if(len(t) == 0):
          return ":"+str(k)+str(v)
        else:
          return str(v)
  u={}
  for k,v in t.items():
    u_len = len(u)
    u[k] = show(k,v)
  if len(t)==0:
    u = sorted(u)
  output = ""
  for key in u:
    output = output + ":" + key + " " + str(u[key]) + " "
  return "{" + output + "}"
  
def oo(t):
  print(o(t))
  return t 

def coerce(s: str) -> int | float | bool | str:
    def fun(s1: str) -> bool | str:
        if s1 == 'true' or s1.lower() == 'true':
            return True
        if s1 == 'false' or s1.lower() == 'false':
            return False
        return s1
    val = s
    try:
        val = float(s)
        if val == int(val):
            val = int(val)
    except ValueError:
        val = fun(re.search('^\s*(.+?)\s*$', s).group(1))
    return val
