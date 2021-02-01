def fibo(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibo(n-2) + fibo(n-1)
		
n = int(input())
if n == 0:
	print(0)
else:
	print(fibo(n))