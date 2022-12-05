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
    
class Outcome(Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors
    
class Lose(Enum):
	A = 3 # Scissors lose to rock
	B = 1 # Rock loses to paper
	C = 2 # Paper loses to scissors

class Win(Enum):
	A = 2 # rock is beaten by paper
	B = 3 # paper is beaten by scissors
	C = 1 # Scissors are beaten by rock
	
def chooseMove(them, outcome): 
	print(them,',',outcome)  
	if outcome == 'Y':
		return them
	elif outcome == 'X':
		return Lose[them]
	else: #if outcome == Z, aka Win
		return Win[them]
		

		
win = {(1,2),(2,3),(3,1)}  

moves = open('input.txt','r').readlines()
moves = [x.strip() for x in moves]

myscores = []


for m in moves:
	t, o = m.split(' ')
	u = Win[chooseMove(t,o)]
	t = Them[t]
	

	#print(o.value,',',u.value)
	if (t.value, u.value) in win:
		myscores.append(u.value + 6)
	elif (t.value, u.value) in win:
		myscores.append(u.value)
	else:
		myscores.append(u.value + 3)
		
print(sum(myscores))

