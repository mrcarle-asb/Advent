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

class Counter(Enum):
    X = {Them.A: 3, Them.B: 1, Them.C: 2} # Lose
    Y = {Them.A: 1+3, Them.B: 2+3, Them.C: 3+3} # Draw
    Z = {Them.A: 2+6, Them.B: 3+6, Them.C: 1+6} # Win


	
def chooseMove(them, outcome): 
	return Counter[outcome].value[Them[them]]	

		
win = {(1,2),(2,3),(3,1)}  

moves = open('input.txt','r').readlines()
moves = [x.strip() for x in moves]

myscores = []


for m in moves:
	t, o = m.split(' ')
	myscores.append(chooseMove(t,o))
	#print(chooseMove(t,o))
	# do stuff with Counter
	
	
print(sum(myscores))

