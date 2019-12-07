
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

f = open('7_puzzle_input.txt', 'r')
line = f.readline()

def IntCode(amp_input, prev_amp_input):
	numbers = line.split(',')
	index = 0
	output = 0
	first_input = True
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

			if first_input == True:
				digit = amp_input
				first_input = False
			else:
				digit = prev_amp_input
			numbers[dest] = int(digit)

		elif opcode == OUTPUT:
			arg1 = int(numbers[index])
			index +=1

			if(arg1mode == POSITION_MODE):
				output = int(numbers[arg1])
			else:
				output = arg1

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
			return output

thruster_values = []
for a_phase in range(0,5):
	for b_phase in range(0,5):
		if b_phase == a_phase:
			continue
		for c_phase in range(0,5):
			if c_phase == b_phase or c_phase == a_phase:
				continue
			for d_phase in range(0,5):
				if d_phase == c_phase or d_phase == b_phase or d_phase == a_phase:
					continue
				for e_phase in range(0,5):
					if e_phase == d_phase or e_phase == c_phase or e_phase == b_phase or e_phase == a_phase:
						continue
					a_output = IntCode(a_phase, 0)
					#print(a_output)
					b_output = IntCode(b_phase, a_output)
					#print(b_output)
					c_output = IntCode(c_phase, b_output)
					#print(c_output)
					d_output = IntCode(d_phase, c_output)
					#print(d_output)
					e_output = IntCode(e_phase, d_output)
					print(e_output)
					thruster_values.append(e_output)

print(max(thruster_values))

# thruster_values = []
# for a in range(0,10):
# 	for b in range(0,10):
# 		for c in range(0,10):
# 			for d in range(0,10):
# 				for e in range(0,10):
# 					print(a,b,c,d,e)
# 					a_output = IntCode(a, 0)
# 					b_output = IntCode(b, a_output)
# 					c_output = IntCode(c, b_output)
# 					d_output = IntCode(d, c_output)
# 					e_output = IntCode(e, d_output)
# 					thruster_values.append(e_output)
#
# print(max(thruster_values))
