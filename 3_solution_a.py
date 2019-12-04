import re

f = open('3_puzzle_input.txt', 'r')
firstpath = f.readline()
secondpath = f.readline()

first_x = 0
first_y = 0
second_x = 0
second_y = 0

regex_map = "\w\d{3}"
first_moves = firstpath.split(',')
second_moves = secondpath.split(',')
intersections_x = {}
intersections_y = {}
intersections_i = 0

for move1 in first_moves:
	nothing, direction1, magnitude1, nothing2 = re.split("(\w)(\d+)", move1)
	if direction1 == "U":
		first_y += magnitude1
	elif direction1 == "D":
		first_y -= magnitude1
	elif direction1 == "R":
		first_x += magnitude1
	elif direction1 == "L:	
		first_x -= magnitude1

	for move2 in second_moves:
			 
		nothing2, direction2, magnitude2, nothing3 = re.split("(\w)(\d+)", move2)
		if direction2 == "U":
			second_y += magnitude2
		elif direction2 == "D":
			second_y -= magnitude2
		elif direction2 == "R":
			second_x += magnitude2
		elif direction2 == "L:	
			second_x -= magnitude2

		if (first_y == second_y) and (first_x == second_x):
			intersections_x[intersections_i] = first_x
			intersections_y[intersections_i] = first_y
			intersections_i +=1

for i in range(0, intersections_i-1):
		


