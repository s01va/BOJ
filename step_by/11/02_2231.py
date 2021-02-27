N_str = input()
N = int(N_str)

N_int = [int(i) for i in N_str]
N_max = N_int[0]-1 + 9*(len(N_int)-1)
flag = False

for i in range(N_max, -1, -1):
	N_tmp = N - i
	N_tmp_int = [int(j) for j in str(N_tmp)]
	if N_tmp + sum(N_tmp_int) == N:
		flag = True
		print(N_tmp)
		break

if flag == False:
	print(0)