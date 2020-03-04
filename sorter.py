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




