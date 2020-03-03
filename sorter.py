def sorter(country_list):
	result = []
	for fst in country_list:
		sortd = sorted(fst, key=lambda x: int(x[1].strip()))
		result.append(sortd)
	return result

