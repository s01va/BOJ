A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
count = [0 for i in range(10)]

for n in result:
	for i in range(10):
		if n == str(i):
			count[i]  = count[i] + 1

for member in count:
	print(member)