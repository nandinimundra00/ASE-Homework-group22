import re
import io
import csv
def fmt(sControl, *args):
  return sControl.format(*args)

def o(t):
    if type(t) != dict and type(t) != list:
        return str(t)

    def fun(k, v):
        if str(k).find("_") != 0:
            v = o(v)
            return ":" + str(k) + " " + o(v)

        else:
            return False

    array = []
    if type(t) == dict:
        for key in t:
            output = fun(key, t[key])
            if output:
                array.append(output)
            array.sort()
    elif type(t) == list:
        array = t
    return "{" + " ".join(str(val) for val in array) + "}"

  
def oo(t):
  print(o(t))
  return t 

def coerce(s: str):
    def fun(s1: str):
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


def cells(s):
    t = []
    for s1 in re.findall("[^,]+", s):
        t.append(coerce(s1))
    return t


def lines(sFilename, fun):
    with open(sFilename, "r") as src:
        for s in src:
            s = s.rstrip("\r\n")
            fun(s)
    src.close()


def CSV(sFilename, fun):
    lines(sFilename, lambda line: fun(cells(line)))
    

fmt = str.format
def say(*args):
    io.stderr.write(fmt(*args))


def sayln(*args):
    io.stderr.write(fmt(*args) + "\n")

def readCSV(sFilename, fun):
       with open(sFilename, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            fun(line)
