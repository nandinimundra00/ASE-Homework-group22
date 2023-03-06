from src.Num import NUM
from src.Sym import *

class COL:
    def __init__(self, n, s):
        self.col = NUM(n, s) if s[0].isupper() else SYM(n, s)
        self.isIgnored = self.col.txt.endswith("X")
        self.isKlass = self.col.txt.endswith("!")
        self.isGoal = self.col.txt[-1] in ["!", "+", "-"]
