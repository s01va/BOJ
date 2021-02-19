N, M = map(int, input().split())
cards_num = sorted(list(map(int, input().split()))[:N], reverse=True)
result = 0

for n1 in cards_num[:len(cards_num)-2]:
	for n2 in cards_num[cards_num.index(n1)+1:len(cards_num)-1]:
		for n3 in cards_num[cards_num.index(n2)+1:]:
			tmpresult = n1 + n2 + n3
			if (tmpresult <= M) and (tmpresult > result):
				result = tmpresult
print(result)