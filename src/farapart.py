from src.data import DATA
from src.l import l

def far():
    d = DATA("../data/auto93.csv")
    a, b, distance, _ = d.farapart(d.rows)
    l_instance = l()
    attempts = 1
    while distance > 0.95 and attempts < 100:
        a, b, distance, _ = d.farapart(d)
        attempts += 1
    print(f'far1: {l_instance.o(a.cells)},\nfar2: {l_instance.o(b.cells)}')
    print(f'distance = {distance}')
    print(f'attempts = {attempts}')

