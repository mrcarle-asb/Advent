import fileinput
import re
from collections import defaultdict, Counter
from enum import Enum #
from itertools import islice, product
# Taking george's imports.  comment on what I think I'm using

class Them(Enum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissors

class Us(Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors
    
win = {(1,2),(2,3),(3,1)}  

moves = open('input.txt','r').readlines()
moves = [x.strip() for x in moves]

myscores = []


for m in moves:
	o, u = m.split(' ')
	o = Them[o]
	u = Us[u]
	#print(o.value,',',u.value)
	if (o.value, u.value) in win:
		myscores.append(u.value + 6)
	elif (u.value, o.value) in win:
		myscores.append(u.value)
	else:
		myscores.append(u.value + 3)
		
print(sum(myscores))

