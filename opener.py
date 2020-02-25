import os

def reader():
	mass = []
	direct = os.scandir("var1")
	for i in direct:
		impermanent_mass = []
		if i.is_file:
			file1 = open(i, 'r')
			for line in file1:
				impermanent_mass.append(line)
		mass.append(impermanent_mass)
	print(mass)
reader()
	

