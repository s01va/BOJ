import math

N = int(input())
tmp = (N - 1 // 6) + 1
answer = (1 + sqrt(1 + tmp)) / 2
print(answer)
