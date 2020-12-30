import sys

N = int(sys.stdin.readline().rstrip().split()[0])
nums = list(map(int, sys.stdin.readline().rstrip().split()))
print(min(nums[:N]), max(nums[:N]))