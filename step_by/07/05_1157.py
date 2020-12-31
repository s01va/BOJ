inputword = input().lower()
setword = list(set(inputword))
frq = [0 for i in range(len(setword))]
for i in range(len(frq)):
	frq[i] = inputword.count(setword[i])

if frq.count(max(frq)) != 1:
	print('?')
else:
	print(setword[frq.index(max(frq))].upper())