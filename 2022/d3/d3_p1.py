from math import floor
rs = open('input.txt','r').readlines()
rs = [x.strip() for x in rs]
priority = "&abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def compareBags(x):
	midp = floor(len(x)/2)
	bag1 = set(item[:midp])
	bag2 = set(item[midp:])
	return(bag1.intersection(bag2))	

def commonBadge(a,b,c):
	elf1 = set(a)
	elf2 = set(b)
	elf3 = set(c)
	return(elf1.intersection(elf2,elf3))

badges = []
for elf, bag in enumerate(rs):
	if (elf+1)%3 == 0:
		badges.append(priority.index(str(commonBadge(rs[elf-2],rs[elf-1],bag).pop()) )    )
	
print(sum(badges))


	