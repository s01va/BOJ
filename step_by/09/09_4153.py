def rtri(x, y, m):
	if x*x + y*y == m*m:
		print("right")
	else:
		print("wrong")

while (True):
	a, b, c = map(int, input().split())
	if a==0 and b==0 and c==0:
		break
	else:
		if max(a, b, c) == a:
			rtri(b, c, a)
		elif max(a, b, c) == b:
			rtri(a, c, b)
		else:
			rtri(a, b, c)