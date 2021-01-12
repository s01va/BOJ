N = int(input())
if N % 5 == 0:
	print(N//5)
else:
	for n5 in range(N//5, -1, -1):
		if (N-5*n5) % 3 == 0:
			print(n5 + ((N-5*n5)//3))
			break
		else:
			if n5 == 0:
				print(-1)