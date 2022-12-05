from math import floor
data = open('input.txt','r').readlines()
data = [x.strip() for x in data]

totalElves = len(data)
djElves = 0
for item in data:
	e1, e2 = item.split(',')
	e1B,e1E = [int(x) for x in e1.split('-')]
	e2B,e2E = [int(x) for x in e2.split('-')]
	e1Set = set(range(e1B, e1E+1))
	e2Set = set(range(e2B, e2E+1))
	if e1Set.isdisjoint(e2Set):
		djElves+=1
	
print(totalElves - djElves)