import sys

#goal: find first floor that causes santa to enter the basement
#
ops = {}
ops['('] = 1
ops[')'] = -1
floor = 0

def helper(op):
	global floor
	global ops
	floor = floor + ops[op]
	return floor

def solve2():
	global floor
	global ops
	thing = []
	lines = sys.stdin.read()
	thing.append(lines[0])
	print(len(lines))
	result = [(x + 1) for x in range(len(lines)) if helper(lines[x]) < 0]
	print('Result: ' + str(result[0]))



#goal: find final floor that santa lands on
def solve():
	floor = 0
	lines = sys.stdin.readlines()
	for line in lines:
		up = line.count('(')
		down = line.count(')')
		floor = floor + (up - down)
	print(floor)


if __name__ == "__main__":
	#solve()
	solve2()