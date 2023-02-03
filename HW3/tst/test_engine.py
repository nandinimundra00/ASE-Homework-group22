from src.Misc import *
from src.Num import *
from src.Sym import *
from src.consts import *
from src.Data import *
global the
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

  def rand_generate_reset_regenerate_same():
      num1, num2 = NUM(), NUM()
      Seed=the['seed']
      for i in range(1, 1000):
        num1.add(rand(0, 1))
      Seed=the['seed']
      for i in range(1, 1000):
        num2.add(rand(0, 1))
      m1 = rnd(num1.mid(), 10)
      m2 = rnd(num2.mid(), 10)
      return m1==m2 and .5 == rnd(m1,1) 

  eg("rand","generate, reset, regenerate same", rand_generate_reset_regenerate_same)
  
  def check_syms():
      sym = SYM()
      for x in ["a", "a", "a", "a", "b", "b", "c"]:
          sym.add(x)
      return "a" == sym.mid() and 1.379 == rnd(sym.div(), 3)

  eg("sym", "check syms", check_syms)

  def check_nums():
      num = NUM()
      for x in [1, 1, 1, 1, 2, 2, 3]:
          num.add(x)
      return 11/7 == num.mid() and 0.787 == rnd(num.div(), 3)

  eg("num", "check nums", check_nums)
    
  def checkReadCSV():
    n = 0
    
    def CsvHelperFunc(t):
      nonlocal n
      n = n+len(t)      
    CSV('data/input.csv', CsvHelperFunc)
    return n == 8*399
  
  eg("csv", "read from csv", checkReadCSV)
  
  def check_data():
    data = DATA('data/input.csv')
    return         len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4
    
  eg("data", "read DATA csv", check_data)


  def checkClone():
    data1 = DATA('data/input.csv')
    data2 = data1.clone(data1.rows)
    return (len(data1.rows) == len(data2.rows)) and data1.cols.y[1].w == data2.cols.y[1].w and data1.cols.x[1].at == data2.cols.x[1].at and (len(data1.cols.x) == len(data2.cols.x))
  
  eg("clone", "duplicate structure", checkClone)

  def checkAround():
    data = DATA('data/input.csv')
    print(0,0,o(data.rows[1]))
    for n, t in enumerate(data.around(data.rows[1])):
      if n%50 == 0:
        print(n, rnd(t['dist'],2) ,o(t['row']))

  eg("around", "sorting nearest neighbors", checkAround)

  def checkHalf():
    data = DATA('data/input.csv')
    left,right,A,B,mid,c = data.half(data.rows) 
    print(len(left),len(right),len(data.rows))
    print(A)
    print(o(A), c)
    print(o(mid))
    print(o(B))

  eg("half", "1-level bi-clustering", checkHalf)

  def checkCluster():
    data = DATA('data/input.csv')
    show(data.cluster(),"mid",data.cols.y,1)

  eg("cluster", "N-level bi-clustering", checkCluster)

  def checkOptimize():
    data = DATA('data/input.csv')
    show(data.sway(),"mid",data.cols.y,1)

  eg("optimize", "semi-supervised optimization", checkOptimize)
  main(the, getConstant("help"), egs)

#   def checkStats():
#     data = DATA('data/input.csv')
#     for k,cols in [('y',data.cols.y),('x',data.cols.x)]:
#       print(k,"mid",o(data.stats("mid",cols,2 )))
#       print("", "div",o(data.stats("div",cols,2)))

#   eg("stats", "stats from DATA", checkStats)

  main(the, getConstant("help"), egs)
