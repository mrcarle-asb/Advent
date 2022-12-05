moves = map(lambda x: x.strip(), open('input.txt','r').readlines() )

def rpsScore(opp,us):
	p1Score = {
			"AX":(1,3),
			"AY":(2,0),
			"AZ":(3,6),
			"BX":(1,0),
			"BY":(2,3),
			"BZ":(3,6),
			"CX":(1,6),
			"CY":(2,0),
			"CZ":(3,3)}
	return sum(p1Score[opp+us])
	
def part1(data):
	myscores = []
	for play in data:
		#print(play)
		opp = play[0]
		ourMove = play[-1]
		#print(opp,"   ,   ",ourMove)
		myscores.append(rpsScore(opp,ourMove))
		#print(myscores[-1])
	print(sum(myscores))

part1(moves)