import os
from sorter import *
def reader():
	teca = input("Введіть назву теки:")
	all_info = []
	direct = os.scandir(teca)
	amount_country = 0
	for i in direct:
		impermanent_mass = []
		if i.is_file and ".csv" in str(i):
			file1 = open(i, 'r')
			for line in file1:
				impermanent_mass.append(line)
		all_info += impermanent_mass[1::]
		amount_country += int(impermanent_mass[0])
	file1.close()
	return(all_info, amount_country)


def column_score(all_info, amount_country):
	column = []
	for i in range(amount_country):
		fx = []
		for j in range(amount_country):
			country_info = all_info[j].split(",")
			fx.append([country_info[0],int(country_info[i+1])])
		column.append(fx)

	return(column)

def main():
	info_list = reader()
	column_s = column_score(info_list[0], info_list[1])
	country_ball = ball(column_s)
	finish(country_ball)

main()
