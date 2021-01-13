N = int(input())
nums = list(map(int, input().split()))
d = 0
for num in nums:
	f = True
	if num == 1:
		f = False
		continue
	for i in range(2, num):
		if num % i == 0:
			f = False
			break
	if f == True:
		d += 1
print(d)