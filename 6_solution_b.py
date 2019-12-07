import re

f = open('6_puzzle_input.txt', 'r')
lines = f.readlines()

planets = {}
indirect_orbits = 0

for line in lines:
    matches = re.split("(\w*).(\w*)", line)
    planet = matches[1]
    orbiting_planet = matches[2]

    # planet.key = child planet
    # planet.value = parent planet
    # root planet will not be listed in planet.keys()
    planets[orbiting_planet] = planet

san_path = []
current_planet = "SAN"
while current_planet in planets.keys():
    san_path.append(current_planet)
    current_planet = planets.get(current_planet)
san_path.append(current_planet)

you_path = []
current_planet = "YOU"
while current_planet in planets.keys():
    you_path.append(current_planet)
    current_planet = planets.get(current_planet)
you_path.append(current_planet)

jumps = {}
for planet in set(you_path).intersection(san_path):
    jumps[planet] = you_path.index(planet) + san_path.index(planet) - 2

print(min(jumps.values()))











