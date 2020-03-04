def sort2(i):
	return i[1]


def ball(score):
	for i in range(len(score)):
		score[i].sort(key=sort2,reverse=True)
		for j in range(len(score[i])):
			if j == 0:
				score[i][j][1] = 12
			elif i == 1:
				score[i][j][1] = 10
			elif j<10:
				score[i][j][1] = 10-j
			else:
				score[i][j][1] = 0
	return score

def finish(score):
	b=[]
	for t in range(len(score)):
		score[t].sort()
	for i in range(1,len(score)):
		for j in range(len(score)):
			score[0][j][1] += score[i][j][1]
	score[0].sort(key = sort2,reverse = True)
	txt = open("result.txt",'w')
	for k in range(10):
		txt.write(str(score[0][k][0] + ',' + str(score[0][k][1]) + '\n\)
	print("\n")
	print(score[0])


