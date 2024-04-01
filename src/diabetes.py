from src.data import DATA
from src.learn import learn

# Test on Diabates
def eg_bayes():
  wme = {"acc":0,"datas":{},"tries":0,"n":0}
  DATA("../data/diabetes.csv", lambda data,t: learn(data,t,wme)) 
  
  print("value:", wme["acc"]/(wme["tries"]))
  print("result:", wme["acc"]/(wme["tries"])> 0.72)

  return wme["acc"]/(wme["tries"]) > 0.72