X = int(input())
N = 1
M = 1
while True:
	if M >= X:
		break
	N += 1
	M = M + N
if N % 2 == 1:
	print(str(M-X+1) + "/" + str(N-M+X))
else:
	print(str(N-M+X) + "/" + str(M-X+1))