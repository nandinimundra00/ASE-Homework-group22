from src.Num import NUM
from src.Sym import *

def COL(n, s):
    # col = NUM(n, s) if s[0].isupper() else SYM(n, s)
    # col['isIgnored'] = 'X' in col['txt']
    # col['isKlass'] = '!' in col['txt']
    # col['isGoal'] = any(x in col['txt'] for x in ['!', '+', '-'])
    # return col
    # col = NUM(n, s) if s.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    #                                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')) else SYM(n, s)
    # col["isIgnored"] = s.endswith('X')
    # col["isKlass"] = s.endswith('!')
    # col["isGoal"] = s.endswith(('!', '+', '-'))
    # return col
    is_num = s[0].isupper()
    col = NUM(n, s) if is_num else SYM(n, s)
    col.isIgnored = s.endswith("X")
    col.isKlass = s.endswith("!")
    col.isGoal = s.endswith("!") or s.endswith("+") or s.endswith("-")
    
    return col
