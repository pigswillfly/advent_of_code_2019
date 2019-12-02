
FINISHED = 99
ADD = 1
MULTIPLY = 2
f = open('2_puzzle_input.txt', 'r')
line = f.readline()
numbers = line.split(',')
numbers[1] = 12
numbers[2] = 2

index = 0
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
	else:
		print(opcode)

print(numbers[0])
	

