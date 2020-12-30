nums = [num for num in range(1, 10001)]

def make_selfnum(num):
	tmpnum = str(num)
	elements = [int(ch) for ch in tmpnum]
	selfnum = num + sum(elements)
	if (selfnum < 10001):
		try:
			nums.remove(selfnum)
		except:
			pass
		make_selfnum(selfnum)

for num in nums:
	make_selfnum(num)

for num in nums:
	print(num)