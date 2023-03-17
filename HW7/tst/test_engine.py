from src.Num import *
from src.consts import *
from src.all_functions import *
from src.Misc import *
import numpy as np
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
  def check_bootmu():
    a = []
    b = []
    for i in range(1, 100):
      a.append(gaussian(10, 1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    for mu in np.linspace(10,11,11):
      b=[]
      for i in range(1,100+1):
          b.append(gaussian(mu,1))
      cl=cliffsDelta(a,b)
      bs=bootstrap(a,b)
      print("",mu,1,cl,bs,cl and bs)  
  eg("bootmu", "check bootmu", check_bootmu)

  def check_basic():
    print("\t\ttruee", bootstrap( {8, 7, 6, 2, 5, 8, 7, 3}, 
                                {8, 7, 6, 2, 5, 8, 7, 3}),
                cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, 
                            {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse", bootstrap(  {8, 7, 6, 2, 5, 8, 7, 3},  
                                    {9, 9, 7, 8, 10, 9, 6}),
                cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3},  
                            {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse", 
                    bootstrap({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}),
                    cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, 
                                {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9})
    )
  eg("basic", "check basic", check_basic)
  def check_pre():
    print("\neg3")
    d = 1
    for i in range(1, 10):
      t1 = []
      t2 = []
      for j in range(1,33):
          t1.append(gaussian(10,1))
          t2.append(gaussian(d * 10,1))
      val = True if d<1.1 else False
      print("\t",d,val,bootstrap(t1,t2),bootstrap(t1,t1))
      d = round(d + 0.05, 2)

  eg("pre", "check pre", check_pre)
  
  def check_five():
   for rx in tiles(scottKnot(
         [RX([0.34,0.49,0.51,0.6,.34,.49,.51,.6],"rx1"),
         RX([0.6,0.7,0.8,0.9,.6,.7,.8,.9],"rx2"),
         RX([0.15,0.25,0.4,0.35,0.15,0.25,0.4,0.35],"rx3"),
         RX([0.6,0.7,0.8,0.9,0.6,0.7,0.8,0.9],"rx4"),
         RX([0.1,0.2,0.3,0.4,0.1,0.2,0.3,0.4],"rx5")])):
    print(rx['name'],rx['rank'],rx['show'])  
    
  eg("five", "check five", check_five)
  main(the, getConstant("help"), egs)
