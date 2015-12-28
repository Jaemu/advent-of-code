import sys

def vowelCount(word):
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowelCount = 0
	for i in xrange(len(word)):
		if(word[i] in vowels):
			vowelCount = vowelCount + 1
		if(vowelCount > 2):
			break
	return (vowelCount > 2)

def solve():
	words = sys.stdin.readlines()
	forbidden = ['ab', 'cd', 'pq', 'xy']
	twice = ['aa','bb','cc','dd','ee','ff', 'gg', 'hh','ii', 'jj', 'kk', 'll', 'mm','nn', 'oo','pp', 'qq', 'rr','ss','tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
	niceWords = [x for x in words for y in forbidden if not y in x]
	actualNiceWords = [x for x in niceWords if vowelCount(x)]
	almostNiceWords = [x for x in actualNiceWords for y in twice if y in x]
	print(actualNiceWords)
	print(str(len(almostNiceWords)) + ', ' + str(len(niceWords)) + ', ' + str(len(actualNiceWords)))

if __name__ == "__main__":
	solve()