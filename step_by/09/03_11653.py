N = int(input())
num = N
for i in range(2, N+1):
	if num == 1:
		break
	while(True):
		if num % i == 0:
			print(i)
			num = num // i
		else:
			break