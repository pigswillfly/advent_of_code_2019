import re

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

FINISHED = 99
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJUST_RELATIVE_BASE = 9

f = open('9_puzzle_input.txt', 'r')
line = f.readline()
thruster_values = []


def IntCode(input, start_index, numbers, relative_base, program_length):
    local_relative_base = relative_base
    index = start_index
    output = 0
    first_input = True
    while index < program_length:
        instruction = str(numbers[index])
        index += 1
        num_digits = len(instruction)
        while num_digits < 5:
            instruction = "0" + instruction
            num_digits += 1

        matches = re.split("(\d)(\d)(\d)(\d+)", instruction)
        arg3mode = int(matches[1])
        arg2mode = int(matches[2])
        arg1mode = int(matches[3])
        opcode = int(matches[4])

        if opcode == ADD:

            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1
            arg3 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                try:
                    src1 = int(numbers[arg1])
                except ValueError:
                    print(arg1)
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if arg3mode == RELATIVE_MODE:
                dest = arg3 + local_relative_base
            else:
                dest = arg3

            numbers[dest] = src1 + src2

        elif opcode == MULTIPLY:

            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1
            arg3 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if arg3mode == RELATIVE_MODE:
                dest = arg3 + local_relative_base
            else:
                dest = arg3

            numbers[dest] = src1 * src2

        elif opcode == INPUT:
            arg1 = int(numbers[index])
            index += 1

            if arg1mode == RELATIVE_MODE:
                src1 = arg1 + local_relative_base
            else:
                src1 = arg1

            numbers[src1] = int(input)

        elif opcode == OUTPUT:
            arg1 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                output = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                output = int(numbers[arg1 + local_relative_base])
            else:
                output = arg1

            print(output)

        elif opcode == JUMP_IF_TRUE:
            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if src1 > 0:
                index = src2

        elif opcode == JUMP_IF_FALSE:
            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if src1 == 0:
                index = src2

        elif opcode == LESS_THAN:
            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1
            arg3 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if arg3mode == RELATIVE_MODE:
                dest = arg3 + local_relative_base
            else:
                dest = arg3

            if src1 < src2:
                store = 1
            else:
                store = 0

            numbers[dest] = store

        elif opcode == EQUALS:
            arg1 = int(numbers[index])
            index += 1
            arg2 = int(numbers[index])
            index += 1
            arg3 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            if arg2mode == POSITION_MODE:
                src2 = int(numbers[arg2])
            elif arg2mode == RELATIVE_MODE:
                src2 = int(numbers[arg2 + local_relative_base])
            else:
                src2 = arg2

            if arg3mode == RELATIVE_MODE:
                dest = arg3 + local_relative_base
            else:
                dest = arg3

            if src1 == src2:
                store = 1
            else:
                store = 0

            numbers[dest] = store

        elif opcode == ADJUST_RELATIVE_BASE:
            arg1 = int(numbers[index])
            index += 1

            if arg1mode == POSITION_MODE:
                src1 = int(numbers[arg1])
            elif arg1mode == RELATIVE_MODE:
                src1 = int(numbers[arg1 + local_relative_base])
            else:
                src1 = arg1

            local_relative_base += src1

        elif opcode == FINISHED:
            return output, local_relative_base


empty_list_items = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
numbers_boost = line.split(',')
original_memory_length = len(numbers_boost)
for i in range(0, 1000):
    numbers_boost.extend(empty_list_items)
boost_output, boost_relative_base = IntCode(2, 0, numbers_boost, 0, original_memory_length)
