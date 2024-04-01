from src.data import DATA

def learn(data,row,my):
  
  my['n'] += 1
  kl   = row.cells[data.cols.klass.at]

  if my['n'] > 10:
      my['tries'] += 1
      my['acc'] += 1 if kl == row.likes(my['datas'])[0] else 0

  if kl not in my['datas']:  
     my['datas'][kl] = DATA(data.cols.names)
  my['datas'][kl].add(row.cells)
  
  return 