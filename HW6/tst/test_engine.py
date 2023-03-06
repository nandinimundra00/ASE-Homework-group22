from src.Misc import *
from src.Num import *
from src.Sym import *
from src.consts import *
from src.Data import *
import json
import ast
from src.query import *
from src.cluster import *
from src.optimization import *
from src.Discretization import *
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
    data = DATA(filenameCSV)
    col = data.cols.x[1].col
    print(col.lo,col.hi, mid(col), div(col))
    print(stats(data))
    
  eg("data", "showing data sets", check_data)
     

  def check_clone():
    data1 = DATA(filenameCSV)
    data2 = DATA(data1, data1.rows)
    print(stats(data1))
    print(stats(data2))
    
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
    dataOBJ = DATA()
    data = dataOBJ.read(filenameCSV)
    num  = NUM()
    for row in data.rows:
        add(num, dist(data, row, data.rows[0]))
    print({"lo": num.lo, "hi": num.hi, "mid": round(mid(num)), "div": round(div(num))})
  
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
    dataOBJ = DATA()
    data = dataOBJ.read(filenameCSV)
    showTree(tree(data))
  eg("tree", "make snd show tree of clusters", check_tree)


  def test_xpln():
    data = DATA(filenameCSV)
    best,rest,evals = sway()
    rule,most= xpln(best,rest)
    print("\n-----------\nexplain=", data.showRule(rule))
    selects = selects(rule,data.rows)
    data_selects = [s for s in selects if s!=None]
    data1= data.clone(data_selects)
    print("all               ",data.stats('mid', data.cols.y, 2),data.stats('div', data.cols.y, 2))
    print("sway with",evals,"evals",best.stats('mid', best.cols.y, 2),best.stats('div', best.cols.y, 2))
    print("xpln on",evals,"evals",data1.stats('mid', data1.cols.y, 2),data1.stats('div', data1.cols.y, 2))
    top,_ = data.betters(len(best.rows))
    top = data.clone(top)
    print("sort with",len(data.rows),"evals",top.stats('mid', top.cols.y, 2),top.stats('div', top.cols.y, 2))
    
  main(the, getConstant("help"), egs)

