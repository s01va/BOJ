inputstr = input()
mintime = 0
for ch in inputstr:
	if (ord(ch) < 83) and (ord(ch) % 3 == 2):
			mintime += (ord(ch) // 3) - 18
	elif ord(ch) == 90:
		mintime += 10
	else: 
		mintime += (ord(ch) // 3) - 19
print(mintime)