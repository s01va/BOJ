import sys

C = int(input())

for i in range(C):
	stdnum_scores = list(map(int, sys.stdin.readline().rstrip().split()))
	stdnum  = stdnum_scores[0]
	scores = stdnum_scores[1:]
	avg = sum(scores) / stdnum
	overavg = 0
	for score in scores:
		if score > avg:
			overavg = overavg + 1
	print("%0.3f%%" % (overavg / stdnum * 100))