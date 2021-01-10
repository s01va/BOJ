A, B, V = map(int, input().rstrip().split())
tmp = (V-B)%(A-B)
if tmp != 0:
	print(((V-B)//(A-B)) + 1)
else:
	print((V-B)//(A-B))