import re
from src.Num import *
from src.Misc import *
from src.Sym import *

class COLS:
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
        for n,s in t.items():
            if re.match("^[A-Z]+", s):                
                col = NUM(n,s)
            else:
                col = SYM(n,s)
            self.all.append(col)
            if not re.search("X$", s):
                if re.search("!$", s):
                    self.klass = col
                if re.search("[!+-]$", s):
                    self.y.append(col)
                else:
                    self.x.append(col)
