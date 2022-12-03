#!python3

import fileinput
import sys
import string
import re
from collections import defaultdict, Counter
from enum import Enum
#from typing import List
#Gilko copy

def count_up(lines):
	total = 0
	bits = Counter()
	for line in lines:
		total +=1
		for i, bit in enumerate(line):
			if bit == '1':
				bits[i] += 1
			#print(bits)
		return total, bits
		
#dataFile = fileinput.input("A3_2_ASB.txt")
dataFile = fileinput.input("A3_Gilko_data.txt")

lines = list( map(lambda x: x.strip(), dataFile) )

def whittle(prefix, most):
	matching = [l for l in lines if l.startswith(prefix)]
	print(prefix, len(matching))
	if len(matching) == 1:
		print("\t", matching[0])
		return int(matching[0],2)
	total, bits = count_up(matching)
	
	i = len(prefix)
	count = bits[i]
	
	if count >= total / 2:
		if most:
			return whittle(prefix + "1",most)
		else:
			return whittle(prefix + "0",most)
	else:
		if most:
			return whittle(prefix + "0",most)
		else:
			return whittle(prefix + "1",most)

o2= whittle("",True)
co2 = whittle("",False)	

print(o2, "*", co2, "=", o2*co2)






#newData=[[row[0] for row in data] if row[0] == filterVals[0]]
# for i in range(len(oxyData[0])):
# 	bitCount = 0
# 	for item in oxyData:
# 		if item[0] == 1:
# 			bitCount+=1
# 		else:
# 			bitCount-=1
# 	if bitCount >= 0:
# 		checkVal = 1
# 	else:
# 		checkVal = 0



# 		 
# 	if len(oxyData)>1:
# 		oxyData = [item for item in oxyData if int(item[i]) == checkVal]
# 		print(oxyData)
# 
# print("oxygen final", oxyData, len(oxyData))
# oxygen=int(oxyData[0],2)

# co2data=data	
# #newData=[[row[0] for row in data] if row[0] == filterVals[0]]
# for i in range(len(data[0])):
# 	checkVal = co2vals[i]
# 	if len(co2data)>1:
# 		co2data = [item for item in co2data if int(item[i]) == checkVal]
# 		#print(newData)
# 
# print("c02 final", co2data, len(co2data))
# co2=int(co2data[0],2)
# print(oxygen)
# print(co2)
# print(oxygen*co2)
		
		
		
		
# Day 3 Part 1 - Correct	



# def opposite(val):
# 	if val == 0:
# 		return 1
# 	else:
# 		return 0
# 
# for index in range(len(data[0])):
# 	for item in data:
# 		if item[index]=="1":
# 			posCount[index]+=1
# 		else:
# 			posCount[index]-=1
# print(len(data[0]))
# print(posCount,", ", filterVals)
# 
# 
# for idx,item in enumerate(posCount):
# 	if item >=0:
# 		filterVals[idx]=1
# 	else:
# 		filterVals[idx]=0
# #print(data,", ",len(data))
# print("O2 vals", filterVals)
# co2vals = [opposite(x) for x in filterVals]
# print("C02", co2vals)

#epsilon="0b"
#gamma="0b"
#posCount=[0,0,0,0,0,0,0,0,0,0,0,0]
#for idx, val in enumerate(data):
#	for i in range(len(val)):
#		if val[i]=="1":
#			posCount[i]+=1
#		else:
#			posCount[i]-=1
#
#for item in posCount:
#	if item > 0:
#		gamma+="1"
#		epsilon+="0"
#	else:
#		gamma+="0"
#		epsilon+="1"
#print(posCount)
#print(gamma, ", ", epsilon)
#print(int(gamma,2)*int(epsilon,2))