import math

def sieve(num):
	if num != 1:
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
	else:
		return False
	return True

while(True):
	n = int(input())
	dn = 0
	if n == 0:
		break
	for m in range(n+1, 2*n+1):
		if sieve(m) == True:
			dn += 1
	print(dn)