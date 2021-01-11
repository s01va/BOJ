import sys
T = int(input())
for i in range(T):
	H, W, N = map(int, sys.stdin.readline().rstrip().split())
	Y = N % H
	if Y == 0:
		Y = str(H)
	else:
		Y = str(Y)
	X = N // H
	if X != N / H:
		X += 1
	if X < 10:
		X = "0"+str(X)
	else:
		X = str(X)
	print(Y + X)