import re
from src.Num import NUM
from src.Misc import *
from src.Sym import *


class COLS:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for c, s in enumerate(names):
            s = str(s)
            if re.match(r"^[A-Z]+", s):
                col = NUM(c, s)
            else:
                col = SYM(c, s)
            self.all.append(col)

            if not re.match(r".*X$", s):
                if (
                    re.match(r".*\+$", s) or re.match(r".*\-$",
                                                      s) or re.match(r".*\!$", s)
                ):
                    self.y.append(col)
                else:
                    self.x.append(col)

                if re.match("!$", s):
                    self.klass = col

    def add(self, row) -> None:
        for t in [self.x, self.y]:
            for i, col in enumerate(t):
                if type(row.cells[i]) is int:
                    col.add(row.cells[i])
