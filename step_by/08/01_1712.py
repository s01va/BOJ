import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())
if (B >= C):
	print(-1)
else:
	N = (A // (C - B)) + 1
	print(N)