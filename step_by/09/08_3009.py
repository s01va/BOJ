sq123 = list()
for i in range(3):
	x, y = map(int, input().split())
	sq123.append([x, y])
if sq123[0][0] == sq123[1][0]:
	rx = sq123[2][0]
elif sq123[0][0] == sq123[2][0]:
	rx = sq123[1][0]
else:
	rx = sq123[0][0]
if sq123[0][1] == sq123[1][1]:
	ry = sq123[2][1]
elif sq123[0][1] == sq123[2][1]:
	ry = sq123[1][1]
else:
	ry = sq123[0][1]
print(rx, ry)