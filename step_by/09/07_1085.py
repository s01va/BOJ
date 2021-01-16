x, y, w, h = map(int, input().split())
if x < w-x:
	d1 = x
else:
	d1 = w-x
if y < h-y:
	d2 = y
else:
	d2 = h-y
if d1 < d2:
	print(d1)
else:
	print(d2)