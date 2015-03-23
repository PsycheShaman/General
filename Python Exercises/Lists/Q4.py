list1 = ['a', 'c', 'g', 't', 't', 'a', 't']

index=0
for item in list1:
	if item == 't':	
		index = list1.index(item, index+1)
		print index
