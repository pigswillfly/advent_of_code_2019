
import re

POSITION_MODE = 0
IMMEDIATE_MODE = 1

FINISHED = 99
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4

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
		numbers[dest] = digit

	elif opcode == OUTPUT:
		arg1 = int(numbers[index])
		index +=1

		if(arg1mode == POSITION_MODE):
			digit = int(numbers[arg1])
		else:
			digit = arg1

		print(digit)

	elif opcode == FINISHED:
		index = len(numbers)
	

