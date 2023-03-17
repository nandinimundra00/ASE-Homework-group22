from src.Num import *
from src.consts import *
from src.all_functions import *
from src.Misc import *
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

  def check_ok():
      print(random.seed(1))
  eg("ok", "check ok", check_ok)


  def check_samples():
      for i in range(10):
        print("", "".join(samples(["a", "b", "c", "d", "e"])))   
  eg("sample", "check samples", check_samples)     
  
  def check_nums():
    n = NUM([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(n.n, n.mu, n.sd)

  eg("num", "check nums", check_nums)
    
  def check_gauss():
    t = []
    for i in range(10 ** 4 + 1):
        t.append(gaussian(10, 2))
    n = NUM(t)
    print(n.n, n.mu, n.sd)

  eg("gauss", "check gaussian", check_gauss)

  main(the, getConstant("help"), egs)
