def get_fuel(number):
	return int(int(number) / 3) - 2

f = open('1_puzzle_input.txt', 'r')
total_fuel = 0
for line in f.readlines():
	fuel = get_fuel(line)
	next_mass = get_fuel(fuel)
	
	while(next_mass > 0):
		fuel += next_mass
		next_mass = get_fuel(next_mass)
		
	total_fuel += fuel

print(total_fuel)
	


