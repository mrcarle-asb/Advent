#!python3


import fileinput
import re
from collections import defaultdict, Counter
import sys
from enum import Enum
from itertools import islice

#Gilko fileinput() structure

dataFile="d4_gilko.txt"
lines = map(lambda x: x.strip(), fileinput.input(dataFile)) #I got hung up here by confusing strip() and split()

draws = list(map(int, next(lines).split(','))) #all draws are on a single long line

next(lines) #burns the blank line between bingo draws and boards



def boards():
	board = []
	for line in lines: #calling global lines, not being passed in
		#print(line)
		if line == "":
			continue   #Like yield but no value returned
		if len(board) == 5:
			yield board  #like a return statement that doesn't end the function
			board = []
		board.append(list(map(int,re.split(" +",line)))) #make a list out of all 
														 #elements in a board line
	yield board #unsure how we get a board here.
	return #null return, syntax requirement to end function

def blank():  # generic results board
	return [
		[False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False],
        [False, False, False, False, False]
	]
def bingo(marks):  # marks is the results matric for each board
	a= [True,True,True,True,True,True,True,True,True,True]
	for i in range(0,5):
		a[0] &= marks[0][i]
		a[1] &= marks[1][i]
		a[2] &= marks[2][i]
		a[3] &= marks[3][i]
		a[4] &= marks[4][i]
		a[5] &= marks[i][0]
		a[6] &= marks[i][1]
		a[7] &= marks[i][2]
		a[8] &= marks[i][3]
		a[9] &= marks[i][4]
	return any(a)




# Part one checks for first board to win, aka smallest index on moves
#Part two checks for last board to win, aka largest index on moves
#
max = 0

answer = 0
for board in boards(): #loop over all boards, checking all draws
	marks = blank()  # Make a results matrix for each boardç
	#print(board)
	for i, draw in enumerate(draws): # for ever draw, loop over all elements of all this board
		for x in range(0,5):
			for y in range(0,5):
				#print("y:", y, "x:", x, "board[y][x]", board[y][x])
				if board[y][x]== draw: 
					marks[y][x] = True
		if bingo(marks): #after each draw, check if there's a bingo on this board
			print(i, draw, board, marks,"\n")
			break # stop working with this board if there's a bingo
					  #break leaves the current loop, taking is back to board in boards
	if i > max: #looking for the fastest bingo
		print("new Record!")
		s=0 #sum of all numbers on board not called by the point of bingo
		for x in range(0,5): #we need to calculate this now
			for y in range(0,5): #because marks doesn't exist outside the loop
				if not marks[y][x]: 
					s+= board[y][x]
		max = i #remember how far we were in the list of draws
		answer = s * draw #multiply the sum by the winning value
			
print(answer)
					
			 
#Working Part 1, check for min
		# 	 if i < min: #looking for the fastest bingo
# 		print("new Record!")
# 		s=0 #sum of all numbers on board not called by the point of bingo
# 		for x in range(0,5): #we need to calculate this now
# 			for y in range(0,5): #because marks doesn't exist outside the loop
# 				if not marks[y][x]: 
# 					s+= board[y][x]
# 		min = i #remember how far we were in the list of draws
# 		answer = s * draw #multiply the sum by the winning value
					