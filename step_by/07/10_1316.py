groupwords = 0
N = int(input())
for i in range(N):
	inputstr = input()
	setstr = list(set(inputstr))
	groupwordOX = True
	for ch in setstr:
		chnum = inputstr.count(ch)
		ch_first = inputstr.find(ch)
		if inputstr.count(ch) > 1:
			if len(set(inputstr[ch_first:ch_first+chnum])) > 1:
				groupwordOX = False
				break
		else:
			pass
	if groupwordOX == True:
		groupwords += 1
print(groupwords)