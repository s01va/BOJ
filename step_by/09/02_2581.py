M = int(input())
N = int(input())
d = list()
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
		d.append(num)
if len(d) == 0:
	print(-1)
else:
	print(sum(d))
	print(d[0])