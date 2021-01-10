N = int(input())
X = 1
while(True):
	if (3 * X * (X - 1) + 1) >= N:
		break
	else:
		X += 1
print(X)