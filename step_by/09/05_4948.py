import math
while(True):
	n = int(input())
	dn = 0
	if n == 0:
		break
	for m in range(n+1, 2*n+1):
		f = True
		if m == 1:
			f = False
			continue
		for i in range(2, int(math.sqrt(m))+1):
			if m % i == 0:
				f = False
				break
		if f == True:
			dn += 1
	print(dn)