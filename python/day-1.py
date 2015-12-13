import sys

def solve():
	floor = 0
	lines = sys.stdin.readlines()
	for line in lines:
		up = line.count('(')
		down = line.count(')')
		floor = floor + (up - down)
	print(floor)


if __name__ == "__main__":
	solve()