from math import floor

data = open('d1_data.txt','r').readlines()


def calcFuel(m):
	fuel = floor(int(m)/3-2)
	if fuel > 0:
		return fuel + calcFuel(fuel)
	else:
		return 0
		
total = sum([calcFuel(mass) for mass in data])
print(total)
