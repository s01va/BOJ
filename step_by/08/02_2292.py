N = int(input())
n = 1
while(True):
	if (3*n*(n-1) + 1) >= N:
		break
	else:
		n+=1
print(n)