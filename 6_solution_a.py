import re

class Planet()


f = open('6_puzzle_input.txt', 'r')
lines = f.readlines()

planets = {}

for line in lines:
    matches = re.split("(\w*).(\w*)", line)
    planet = matches[1]
    orbiting_planet = matches[2]

    if planets[planet]







print(planets)


