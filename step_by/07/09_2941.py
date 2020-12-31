croatiach = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
inputstr = input()
for ch in croatiach:
	inputstr = inputstr.replace(ch, '*')
print(len(inputstr))