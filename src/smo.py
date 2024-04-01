from src.l import l
from src.data import DATA
from src.row import ROW

def gate20():
  BUDGET0 = 4
  BUDGET = 16   
  SOME = 0.5 

  print1 = []
  print2 = []
  print3 = []
  print4 = []
  print5 = []
  print6 = []
  
  for i in range(20):
    d = DATA("../data/auto93.csv")

    stats, bests, row1, row2, row3, row4, row5, row6 = d.gate(BUDGET0, BUDGET, SOME)
    # stat, best = stats[-1], bests[-1]
    # print(l().rnd(best.d2h(d)), l().rnd(stat.d2h(d)))
    print1 += row1
    print2 += row2
    print3 += row3
    print4 += row4
    print5 += row5
    print6 += row6

  print("Print 1: top6\n", print1)
  print("====================================")
  print("Print 2: top50\n", print2)
  print("====================================")
  print("Print 3: most\n", print3)
  print("====================================")
  print("Print 4: rand\n", print4)
  print("====================================")
  print("Print 5: mid\n", print5)
  print("====================================")
  print("Print 6: top\n", print6)
  print("====================================")
