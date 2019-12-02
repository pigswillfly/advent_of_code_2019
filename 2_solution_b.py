
FINISHED = 99
ADD = 1
MULTIPLY = 2
DESIRED_OUTPUT = 19690720
f = open('2_puzzle_input.txt', 'r')
line = f.readline()
numbers = line.split(',')
index = 0

for noun in range(0, 99):
	for verb in range(0, 99):
		numbers[1] = noun
		numbers[2] = verb
	
		while index < len(numbers):
			opcode = int(numbers[index])
			index+=1
			src1 = int(numbers[index])
			index+=1
			src2 = int(numbers[index])
			index+=1	
			dest = int(numbers[index])
			index+=1

			if opcode == ADD:
				numbers[dest] = int(numbers[src1]) + int(numbers[src2])
			elif opcode == MULTIPLY:
				numbers[dest] = int(numbers[src1]) * int(numbers[src2])
			elif opcode == FINISHED:
				index = len(numbers)

		output = int(numbers[0])
		if(output == DESIRED_OUTPUT):
			print(100 * noun + verb)
			break
		else:
			numbers = {}
			numbers = line.split(',')
			index = 0
	if(output == DESIRED_OUTPUT):
		break
