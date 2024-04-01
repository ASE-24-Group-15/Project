from datetime import datetime
from email.mime import base
from logging import config
import random
from statistics import stdev
from src.stats import SAMPLE, eg0
from src.data import DATA
from src.l import l
import src.config as config

def generateStats():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")
    print("seed : ", config.the.seed)
    
    data = DATA(config.the.file)
    print("rows : ", len(data.rows))
    print("cols : ", len(data.cols.names[0]))
    print("names \t\t\t\t", '[' + ', '.join(["'" + item + "'" for item in data.cols.names[0]]) + ']' + "\t\td2h-")
    dataMid = data.mid()
    dataDiv = data.div()
    print("mid \t\t\t\t", '[' + ', '.join(["'" + str(l.rnd(2, item)) + "'" for item in dataMid.cells]) + ']' + "\t\t" + str(l.rnd(2, dataMid.d2h(data))))
    print("div \t\t\t\t", '[' + ', '.join(["'" + str(l.rnd(2, item)) + "'" for item in dataDiv.cells]) + ']' + "\t\t" + str(l.rnd(2, dataDiv.d2h(data))))
    print("#")
    
    #running smo9 20 times
    for _ in range(20):
        _, best = data.gate(4, 9, 0.5)
        print("smo9 \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in best[-1].cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, best[-1].d2h(data))))
    
    print("#")
    
    #running any50
    for _ in range(20):
        rand50 = random.sample(data.rows, 50)
        rows = sorted(rand50, key=lambda x: x.d2h(data))
        print("any50 \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in rows[0].cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, rows[0].d2h(data))))
        
    print("#")
    
    #all data
    bestRow = sorted(data.rows, key=lambda x: x.d2h(data))[0]
    print("100% \t\t\t\t", '[' + ', '.join(["'" + str(item) + "'" for item in bestRow.cells]) + ']' + "\t\t\t\t" + str(l.rnd(2, bestRow.d2h(data))))
    

def bonr(n):
    bestList = []
    for i in range(20):
        data = DATA(config.the.file)
        _, best = data.gate(4, n-4, 0.5)
        bestList.append(best[-1].d2h(data))
    return bestList
    
def rand(n):
    randList = []
    for i in range(20):
        data = DATA(config.the.file)
        randRows = random.sample(data.rows, n)
        rows = sorted(randRows, key=lambda x: x.d2h(data))
        randList.append(rows[0].d2h(data))
    return randList

def best_tiny():
    data = DATA(config.the.file)
    sortedRows =  sorted(data.rows, key=lambda x: x.d2h(data))
    baseLines = [row.d2h(data) for row in data.rows]
    return sortedRows[0].d2h(data), stdev(baseLines) * 0.35, baseLines

    
def experimentTreatments():
    print("date : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file : ", config.the.file)
    print("repeats : 20")
    print("seed : ", config.the.seed)
    data = DATA(config.the.file)
    print("rows : ", len(data.rows))
    print("cols : ", len(data.cols.names[0]))
    print("#base #bonr9 #rand9 #bonr15 #rand15 #bonr20 #rand20 #rand358 ")
    best, tiny, baseLines = best_tiny()
    print("best : ", l.rnd(2, best))
    print("tiny : ", l.rnd(2, tiny))
    eg0([
        SAMPLE(bonr(9), "bonr9"),
        SAMPLE(rand(9), "rand9"),
        SAMPLE(bonr(15), "bonr15"),
        SAMPLE(rand(15), "rand15"), 
        SAMPLE(bonr(20), "bonr20"),
        SAMPLE(rand(20), "rand20"), 
        SAMPLE(rand(358), "rand358"), 
        SAMPLE(baseLines, "base")
    ])