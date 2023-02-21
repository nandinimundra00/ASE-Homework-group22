from src.Misc import *
from src.Num import *
from src.Sym import *
from src.consts import *
from src.Data import *
import json
import ast
from src.query import *
from src.cluster import *
filenameCSV = 'data/input.csv'

def run_tests():

  def main(options, help, funs):
      saved = {}
      fails = 0
      
      for k,v in cli(settings(help)).items():
        options[k] = v
        saved[k] = v
      print("main options", options)
      if options["help"]:
        print(help)
      else:
        for what, fun in funs.items():
          if options["go"] == "all" or what == options["go"]:
            for k, v in saved.items():
              options[k] = v
            Seed = options["seed"]
            if funs[what]()== False:
              fails=fails+1
              print("❌ fail:",what)
            else:
              print("✅ pass:",what)
      
      exit(fails)

  #egs

  egs = {}
  the = {}
  def eg(key, str, fun):
    egs[key] = fun
    help = getConstant("help")
    help = help + " -g {}\t{}\n".format(key, str)

  eg("the", "show settings", lambda:oo(the))

  def check_random():

    t = []
    u = []
    Seed=the['seed']
    for i in range(1, 1000):
      push(t, rint(100))
    Seed=the['seed']
    for i in range(1, 1000):
      push(u, rint(100))
      
    for k, v in enumerate(t):
      assert(v==u[k])
      
  eg("rand", "demo random number generation", check_random)


  def check_some():
    max = 32
    num1 = NUM()
    for i in range(1,10000):
      add(num1,i)
    oo(has(num1))
    
  eg("some", "demo of reservoir sampling", check_some)
  
  
  def check_nums():
    num1 = NUM()
    num2 = NUM()

    for i in range(10000):
      add(num1, rand()) 
    for i in range(10000):
      add(num2, rand()** 2) 
    print(mid(num1))
    print(1, rnd(mid(num1)), rnd(div(num1)))
    print(2, rnd(mid(num2)), rnd(div(num2)))
    return .5 == rnd(mid(num1)) and mid(num1) > mid(num2) 
  
  # eg("nums", "demo of NUM", check_nums)
  
  def check_syms():
    
    sym=adds(SYM(), ["a", "a", "a", "a", "b", "b", "c"])
    print(mid(sym), rnd(div(sym)))
    return 1.38 == rnd(div(sym))
  
  eg("syms", "demo SYMS", check_syms)
  


    
  def check_csv():
    n = 0
    def CsvHelperFunc(t):
      nonlocal n
      n = n+len(t)

    CSV(filenameCSV, CsvHelperFunc)
  
    return 3192 == n 

  eg("csv", "reading csv files SYMS", check_csv)
  
  def check_data():
    data = read(filenameCSV)
    # print(data)
    col = data["cols"]["x"][1]
    print(col.lo, col.hi, mid(col), div(col))
    oo(stats(data))
    
  eg("data", "showing data sets", check_data)
     

  def check_clone():
    data1 = read(filenameCSV)
    data2= clone(data1, data1['rows'])
    oo(stats(data1))
    oo(stats(data2)) 
    
  eg("clone", "replicate structure of a DATA",check_clone)
   
  def check_cliffs():
    assert cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]) == False, "1"
    assert cliffsDelta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]) == True, "2"
    t1 = []
    t2 = []
    for i in range(0, 1000):
      t1.append(random.random())
      t2.append(random.random() ** 0.5)
    assert cliffsDelta(t1, t1) == False, "3"
    assert cliffsDelta(t1, t2) == True, "4"
    diff = False
    j = 1.0
    while not diff:
        t3 = list(map(lambda x: x*j, t1))
        diff = cliffsDelta(t1, t3)
        print(">", round(j, 4), diff)
        j *= 1.025      
  eg("cliffs", "stats test", check_cliffs)

  def distance_test():
    data = read(filenameCSV)
    num = NUM()
    for row in data['rows']:
        add(num, dist(data, row, data['rows'][0]))
  #to add oo()!!
  eg("dist", "distance test", distance_test)

  # def check_half():
  #   data = read(filenameCSV)
  #   left, right, A, B, c = half(data)
  #   print(len(left), len(right))
  #   l, r = clone(data, left), clone(data, right)
  #   print("l", o(stats(l)))
  #   print("r", o(stats(r)))
  # eg("half", "divide data in halg", check_half)

  # go("tree","make snd show tree of clusters", function(   data,l,r)
  # showTree(tree(DATA.read(the.file))) end)

  def check_tree():
    showTree(tree(read(filenameCSV)))
  eg("tree", "make snd show tree of clusters", check_tree)

  # def check_copy():
  #   t1 = {"a": 1,
  #         "b": {"c": 2, "d": {3}}
  #         }
  #   t2 = deepcopy(t1)
  #   t2["b"]["d"] = {10000}
  #   print("b4", o(t1))
  #   print("After", o(t2))

  # eg("copy", "check copy", check_copy)


  # def check_syms():
  #     sym = SYM()
  #     for x in ["a", "a", "a", "a", "b", "b", "c"]:
  #         sym.add(x)
  #     return "a" == sym.mid() and 1.379 == rnd(sym.div(), 3)

  # eg("sym", "check syms", check_syms)

  # def check_nums():
  #     num = NUM()
  #     for x in [1, 1, 1, 1, 2, 2, 3]:
  #         num.add(x)
  #     return 11/7 == num.mid() and 0.787 == rnd(num.div(), 3)

  # eg("num", "check nums", check_nums)
  

    
  main(the, getConstant("help"), egs)

