import re
from src.Num import NUM
from src.Misc import *
from src.Sym import *
from src.Col import COL

# class COLS:
#     def __init__(self, names):
#         self.names = names
#         self.all = []
#         self.klass = None
#         self.x = []
#         self.y = []

#         for c, s in enumerate(names):
#             s = str(s)
#             if re.match(r"^[A-Z]+", s):
#                 col = NUM(c, s)
#             else:
#                 col = SYM(c, s)
#             self.all.append(col)

#             if not re.match(r".*X$", s):
#                 if (
#                     re.match(r".*\+$", s) or re.match(r".*\-$", s) or re.match(r".*\!$", s)
#                 ):
#                     self.y.append(col)
#                 else:
#                     self.x.append(col)

#                 if re.match("!$", s):
#                     self.klass = col

#     def add(self, row) -> None:
#         for t in [self.x, self.y]:
#             for i,col in enumerate(t):
#                 if type(row.cells[i]) is int:
#                     col.add(row.cells[i])

def COLS(ss):
    cols = {"names": ss, "all": [], "x": [], "y": []}
    for n, s in enumerate(ss):
        col = COL(n, s)
        
        cols["all"].append(col)
        if not col.isIgnored:
            if col.isKlass:
                cols["klass"] = col
            if col.isGoal:
                cols["y"].append(col)
            else:
                cols["x"].append(col)
    return cols
    

def RANGE(at,txt,lo,hi = None):
    if hi is None:
        hi = lo
    y = SYM()
    return {'at': at, 'txt': txt, 'lo': lo, 'hi': hi, 'y': y}

