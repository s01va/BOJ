import sys

S = input()
atoz = [chr(c) for c in range(ord('a'), ord('z') + 1)]
for ch in atoz:
	sys.stdout.write(str(S.find(ch)) + " ")