f = open('1_puzzle_input.txt', 'r')
total_fuel = 0
for line in f.readlines():
	fuel = int(int(line) / 3) - 2
	total_fuel += fuel

print(total_fuel)
	
