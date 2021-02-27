N = int(input())
Nlist = list()

for i in range(N):
	x, y = map(int, input().split())
	Nlist.append([x, y])
Nrank = [1 for i in range(len(Nlist))]
for i in range(0,len(Nlist)-1):
	for j in range(i+1,len(Nlist)):
		if Nlist[i][0] < Nlist[j][0] and Nlist[i][1] < Nlist[j][1]:
			Nrank[i] += 1
		elif Nlist[i][0] > Nlist[j][0] and Nlist[i][1] > Nlist[j][1]:
			Nrank[j] += 1
result = ""
for i in Nrank:
	result = result + " " + str(i)
print(result.strip())