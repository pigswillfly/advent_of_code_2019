
import re

POSITION_MODE = 0
IMMEDIATE_MODE = 1

FINISHED = 99
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

f = open('5_puzzle_input.txt', 'r')
line = f.readline()
numbers = line.split(',')
index = 0
	
while index < len(numbers):
	instruction = str(numbers[index])
	index +=1
	num_digits = len(instruction)
	while num_digits < 5:
		instruction = "0" + instruction
		num_digits +=1
	
	matches = re.split("(\d)(\d)(\d)(\d+)", instruction)
	arg3mode = int(matches[1])
	arg2mode = int(matches[2])
	arg1mode = int(matches[3])	
	opcode = int(matches[4])	

	if opcode == ADD:

		arg1 = int(numbers[index])
		index+=1
		arg2 = int(numbers[index])
		index+=1	
		arg3 = int(numbers[index])
		index+=1			

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		dest = arg3

		numbers[dest] = src1 + src2

	elif opcode == MULTIPLY:

		arg1 = int(numbers[index])
		index+=1
		arg2 = int(numbers[index])
		index+=1	
		arg3 = int(numbers[index])
		index+=1			

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		dest = arg3
		numbers[dest] = src1 * src2

	elif opcode == INPUT:
		dest = int(numbers[index])
		index +=1

		print("Give an input: ")
		digit = input()
		numbers[dest] = int(digit)

	elif opcode == OUTPUT:
		arg1 = int(numbers[index])
		index +=1

		if(arg1mode == POSITION_MODE):
			digit = int(numbers[arg1])
		else:
			digit = arg1

		print(digit)

	elif opcode == JUMP_IF_TRUE:
		arg1 = int(numbers[index])
		index +=1
		arg2 = int(numbers[index])
		index +=1

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		if(src1 > 0):
			index = src2

	elif opcode == JUMP_IF_FALSE:	
		arg1 = int(numbers[index])
		index +=1
		arg2 = int(numbers[index])
		index +=1

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		if(src1 == 0):
			index = src2

	elif opcode == LESS_THAN:
		arg1 = int(numbers[index])
		index+=1
		arg2 = int(numbers[index])
		index+=1	
		arg3 = int(numbers[index])
		index+=1			

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		dest = arg3

		if(src1 < src2):
			store = 1
		else:
			store = 0

		numbers[dest] = store

	elif opcode == EQUALS:
		arg1 = int(numbers[index])
		index+=1
		arg2 = int(numbers[index])
		index+=1	
		arg3 = int(numbers[index])
		index+=1			

		if(arg1mode == POSITION_MODE):
			src1 = int(numbers[arg1])
		else:
			src1 = arg1

		if(arg2mode == POSITION_MODE):
			src2 = int(numbers[arg2])
		else:
			src2 = arg2

		dest = arg3

		if(src1 == src2):
			store = 1
		else:
			store = 0

		numbers[dest] = store
	elif opcode == FINISHED:
		index = len(numbers)
	

