import sys

subject_num = int(input())
maxscore = 0
rscores = []

scores = list(map(int, sys.stdin.readline().rstrip().split()))[:subject_num]

maxscore = max(scores)

for score in scores:
	rscores.append(score/maxscore*100)

print(sum(rscores)/len(rscores))
