import re

f = open('10_puzzle_input.txt', 'r')
lines = f.readlines()

Y_MAX = len(lines)
X_MAX = len(lines[0]) - 1

field = []
y = 0
for line in lines:
    x = 0
    for asteroid in line:
        if asteroid == '\n':
            continue
        field.append((x, y, asteroid))
        x += 1
    y += 1

print(field)


