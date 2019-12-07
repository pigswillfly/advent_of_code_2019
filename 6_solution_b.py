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

for child, parent in planets.items():
    indirect_orbits += 1

    while parent in planets.keys():
        indirect_orbits += 1
        parent = planets.get(parent)

print(indirect_orbits)


