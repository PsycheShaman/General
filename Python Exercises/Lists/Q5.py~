from types import *
print 'please enter a maximum of 5 pairs of coordinates (x:y), between 0 and 4... leave x blank to terminate sequence: '

i=0
list1 = []
while i < 5:
	X = raw_input('X> ')
	Y = raw_input('Y> ')
	try:
		X = int(X)
		Y = int(Y)
		if 0 <= X <= 4 and 0 <= Y <= 4:
			tuple1 = (X, Y)
			list1.append(tuple1)
		else:
			print 'coordinate not within boundary'
		i+=1
	except ValueError:
		print 'done'
		break		
			
grid = [['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#']]

for item in list1:
	x = item[0]
	y = item[1]
	grid[y][x] = ' '

for line in grid:
	print line
