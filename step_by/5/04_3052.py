result = list()

for i in range(10):
	tmp = int(input())
	result.append(tmp % 42)

result = set(result)
print(len(result))