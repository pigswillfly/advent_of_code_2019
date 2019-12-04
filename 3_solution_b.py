import re

f = open('3_puzzle_input.txt', 'r')
firstpath = f.readline()
secondpath = f.readline()

first_x = 0
first_y = 0
second_x = 0
second_y = 0

first_moves = firstpath.split(',')
second_moves = secondpath.split(',')

first_coords = []
second_coords = []
intersect_coords = []
index = 0

for move1 in first_moves:
	nothing, direction1, magnitude1, nothing2 = re.split("(\w)(\d+)", move1)
	mag1 = int(magnitude1)
	if direction1 == "U":
		for i in range(index, index+mag1):
			first_y += 1
			first_coords.append((first_x, first_y))
	elif direction1 == "D":
		for i in range(index, index+mag1):
			first_y -= 1
			first_coords.append((first_x, first_y))
	elif direction1 == "R":
		for i in range(index, index+mag1):
			first_x += 1
			first_coords.append((first_x, first_y))
	elif direction1 == "L":
		for i in range(index, index+mag1):
			first_x -= 1
			first_coords.append((first_x, first_y))
	index += mag1

index = 0
for move2 in second_moves:
	nothing2, direction2, magnitude2, nothing3 = re.split("(\w)(\d+)", move2)
	mag2 = int(magnitude2)
	if direction2 == "U":
		for i in range(index, index+mag2):
			second_y += 1
			second_coords.append((second_x, second_y))
	elif direction2 == "D":
		for i in range(index, index+mag2):
			second_y -= 1
			second_coords.append((second_x, second_y))
	elif direction2 == "R":
		for i in range(index, index+mag2):
			second_x += 1
			second_coords.append((second_x, second_y))
	elif direction2 == "L":	
		for i in range(index, index+mag2):
			second_x -= 1
			second_coords.append((second_x, second_y))
	index += mag2	

man_dist = []
steps_taken = []
for coord in set(first_coords).intersection(second_coords):
	man_dist.append(abs(coord[0]) + abs(coord[1]))
	steps_taken.append(first_coords.index(coord)+1 + second_coords.index(coord)+1)

print(min(steps_taken))
