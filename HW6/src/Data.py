from src.Misc import *
from src.Cols import *
from src.Row import *
from src.list_util import *
from src.consts import *
from operator import itemgetter
from collections.abc import Iterable
import random
import re
from src.str_util import *
from src.Cols import COLS
from src.query import *
from src.helpdict import *
from src.update import *

class DATA:

    def __init__(self, src, rows = None):
        self.rows = []
        self.cols = None
        add = lambda t: row(self, t)
        if isinstance(src, str):
            readCSV(src, add)
        else:
            self.cols = COLS(src.cols.names)
            if rows:
                for row in rows:
                    add(row)

    def read(self, sFile):
        data = DATA()
        callback = lambda t: row(data, t)
        readCSV(sFile, callback)
        return data

    def clone(self, data, ts = None):
        data1 = row(DATA(), data.cols.names)
        for t in (ts or []):
            row(data1, t)
        return data1
