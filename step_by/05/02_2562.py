nums = list()
for i in range(9):
	nums.append(int(input()))
maxnum = max(nums)
print(maxnum)
print(nums.index(maxnum) + 1)