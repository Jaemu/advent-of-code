import sys

def solve():
	moveList = sys.stdin.read().strip()
	moves = {}

	houseGrid = []
	houseGrid.append([1])

	moves['^'] = [-1, 0]
	moves['v'] = [1, 0]
	moves['<'] = [0, -1]
	moves['>'] = [0, 1]
	santa = {}
	santa['x'] = 0
	santa['y'] = 0
	robo = {}
	robo['x'] = 0
	robo['y'] = 0
	santaList = [(0,0)]
	isSanta = True
	for move in moveList:
		currentMove = moves[move]
		if(isSanta):
			isSanta = False
			santa['y'] = santa['y'] + currentMove[0]
			santa['x'] = santa['x'] + currentMove[1]
			currentPosition = (santa['y'], santa['x'])
			if not currentPosition in santaList:
				santaList.append(currentPosition)
		else:
			isSanta = True
			robo['y'] = robo['y'] + currentMove[0]
			robo['x'] = robo['x'] + currentMove[1]
			currentPosition = (robo['y'], robo['x'])
			if not currentPosition in santaList:
				santaList.append(currentPosition)
	print(str(len(santaList)))



if __name__ == "__main__":
	solve()