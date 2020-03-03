import os
from sorter import sorter

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
	return(all_info, amount_country)


def column_score(all_info, amount_country):
	column = []
	for i in range(amount_country):
		fx = []
		for j in range(amount_country):
			country_info = all_info[j].split(",")
			fx.append([country_info[0],country_info[i+1]])
		column.append(fx)
	print(column)
	return column


if __name__ == "__main__":
	a = reader()
	info = column_score(a[0], a[1])
	res = sorter(info)
	print(res)

