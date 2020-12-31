import sys

T = int(input())
for testcase in range(T):
	R, S = sys.stdin.readline().rstrip().split()
	R = int(R)
	P = ""
	for ch in S:
		for i in range(R):
			P += ch
	print(P)