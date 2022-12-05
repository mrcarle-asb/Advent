from math import floor
data = open('input.txt','r').readlines()
data = [x.strip() for x in data]

fullSubSets = 0
for item in data:
	e1, e2 = item.split(',')
	e1B,e1E = [int(x) for x in e1.split('-')]
	e2B,e2E = [int(x) for x in e2.split('-')]
	e1Set = set(range(e1B, e1E+1))
	e2Set = set(range(e2B, e2E+1))
	if e1Set.issubset(e2Set) or e2Set.issubset(e1Set):
		fullSubSets+=1

print(fullSubSets)