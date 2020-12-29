N = int(input())

scores = []
for i in range(N):
	score = 0
	testcase = input()
	o = 0
	for ox in testcase:
		if ox == 'O':
			o = o + 1
		elif ox == 'X':
			o = 0
		score = score + o
	scores.append(score)

for score in scores:
	print(score)