import sys
M, N = map(int, sys.stdin.readline().rstrip().split())
for num in range(M,N+1):
	f = True
	if num == 1:
		f = False
		continue
	for n in range(2, num):
		if num % n == 0:
			f = False
			break
	if f == True:
		sys.stdout.write(str(num) + "\n")