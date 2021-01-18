import math
T = int(input())
for t in range(T):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	if x1 == x2 and y1 == y2:
		if r1 == r2:
			print(-1)
		else:
			print(0)
	else:
		d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
		if (d == r1 + r2) or (d == abs(r1 - r2)):
			print(1)
		elif (d > abs(r1 - r2)) and  (d < r1 + r2):
			print(2)
		else:
			print(0)