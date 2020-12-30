import sys

while(True):
	try:
		A, B = sys.stdin.readline().rstrip().split()
		if (int(A) > 0) or (int(B) < 10):
			sys.stdout.write(str(int(A) + int(B)) + "\n")
		else:
			break
	except:
		break