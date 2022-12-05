data = open('d1_data.txt','r').readlines()


'''   Part 1 Solutiton
elfCalTotal = 0
elfCalMax = 0


for lineNum, line in enumerate(data):
	if line == "\n":
		print(lineNum, " is blank.")
		if elfCalTotal > elfCalMax:
			elfCalMax = elfCalTotal
			print(elfCalMax)
		elfCalTotal = 0
	else:
		#print(line)
		elfCalTotal+=int(line.strip())
		#print(elfCalTotal)
'''

elfCal = 0
elfList = []

for lineNum, line in enumerate(data):
	if line == "\n":
		#print(lineNum, " is blank.")
		elfList.append(elfCal)
		#print(elfList[-1])
		elfCal = 0
		
	else:
		#print(line)
		elfCal+=int(line.strip())
		#print(elfCalTotal)
elfList.sort()
print(sum(elfList[-3:]))
