N = int(input())
hnum_n = 0

for num in range(1, N+1):
	elements = [int(ch) for ch in str(num)]
	if len(elements) < 2:
		hnum_n += 1
	else:
		gap = elements[1] - elements[0]
		ishan = True
		for i in range(2, len(elements)):
			if (elements[i] - elements[i-1]) != gap:
				ishan = False
				break
		if ishan == True:
			hnum_n += 1

print(hnum_n)