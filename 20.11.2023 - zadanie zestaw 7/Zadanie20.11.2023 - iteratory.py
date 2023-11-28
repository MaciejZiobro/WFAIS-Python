import itertools
import random

iter1 = itertools.cycle([0,1])
iter_zeros2 = iter((lambda: 0), 1)  
Directions = ["N", "E", "S", "W"]
iter2 = (Directions[random.choice(range(4))] for _ in iter(int, 1))
#tab1 = []
#for i in iter2:
#    if len(tab1)<20:
#        tab1.append(i)
#    else: break
#print(tab1)

iter31 = itertools.cycle([0,1,2,3,4,5,6])
iter32 = itertools.cycle(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
#tab2 = []
#for i in iter32:
#    if len(tab2)<100:
#        tab2.append(i)
#    else: break
#print(tab2)
