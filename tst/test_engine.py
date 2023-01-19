from src.Misc import *
from src.Num import *
from src.Sym import *
from src.consts import *
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
      
  main(the, getConstant("help"), egs)
