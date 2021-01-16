import math

def sieve(num):
	if num != 1:
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
	else:
		return False
	return True

T = int(input())
for t in range(T):
	N = int(input())
	pv = N // 2
	for i in range(pv, 1, -1):
		if sieve(i) == True:
			if sieve(N - i) == True:
				print(str(i) + " " + str(N - i))
				break
