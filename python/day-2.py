import sys

def area(x,y,z):
	a1 = x * y
	a2 = y * z
	a3 = x * z
	return (((2 *a1) + (2*a2) + (2*a3)) + min(a1, a2, a3))

def ribbon(lwh):
	lwhCopy = lwh[:]
	a1 = 2 * min(lwh)
	lwhCopy.pop(lwhCopy.index(min(lwhCopy)))
	a2 = 2 * min(lwhCopy)
	return (a1 + a2 + (lwh[0] * lwh[1] * lwh[2]))

def solve2():
	boxes = sys.stdin.readlines()
	boxes = [y.strip('\n').split('x') for y in boxes]
	result = [ribbon([int(box[0]),int(box[1]),int(box[2])]) for box in boxes]
	print(str(sum(result)))

#goal: find final floor that santa lands on
def solve():
	boxes = sys.stdin.readlines()
	boxes = [y.strip('\n').split('x') for y in boxes]
	result = [area(int(box[0]),int(box[1]),int(box[2])) for box in boxes]
	print(str(sum(result)))

if __name__ == "__main__":
	#solve()
	solve2()