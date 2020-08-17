def nested_sum(list):
    total = 0
    for value in list:
        for val in value:
            total += val
            
    return total

print(nested_sum([[1, 2, 3], [4, 5]]))

ddef fancy_concatenate(lists):
	total = ""
	for list in lists:
		if len(list) != 3:
			continue
		else:
			for string in list:
				total += string
				
	return total