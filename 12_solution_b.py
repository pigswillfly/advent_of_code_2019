import re
from itertools import combinations
from math import gcd

f = open('12_puzzle_input.txt', 'r')
lines = f.readlines()

STEPS = 1000
NUM_MOONS = 4


def reset_system(position, velocity):
    index = 0
    for line in lines:
        axes = re.split("<x=(.+), y=(.+), z=(.+)>", line)
        position[index] = [int(axes[1]), int(axes[2]), int(axes[3])]
        velocity[index] = [0, 0, 0]
        index += 1


def apply_gravity(moon_a, moon_b, axis, position, velocity):
    if position[moon_a][axis] > position[moon_b][axis]:
        velocity[moon_a][axis] -= 1
        velocity[moon_b][axis] += 1
    elif position[moon_a][axis] < position[moon_b][axis]:
        velocity[moon_a][axis] += 1
        velocity[moon_b][axis] -= 1


def apply_velocity(moon, axis, position, velocity):
    position[moon][axis] += velocity[moon][axis]


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


position = {}
velocity = {}
reset_system(position, velocity)
moon_combos = list(combinations(position.keys(), 2))
position_repeated = False
steps_to_repeat = [0, 0, 0]
initial_position = {}
for m in range(0, NUM_MOONS):
    initial_position[m] = [position[m][0], position[m][1], position[m][2]]

for a in range(0, 3):
    position_repeated = False
    s = 0
    while not position_repeated:
        for c in range(0, len(moon_combos)):
            apply_gravity(moon_combos[c][0], moon_combos[c][1], a, position, velocity)
        for m in range(0, NUM_MOONS):
            apply_velocity(m, a, position, velocity)
        s += 1
        if position[0][a] == initial_position[0][a]:
            if position[1][a] == initial_position[1][a]:
                if position[2][a] == initial_position[2][a]:
                    if position[3][a] == initial_position[3][a]:
                        position_repeated = True
                        steps_to_repeat[a] = s+1
    reset_system(position, velocity)
lcm1 = lcm(steps_to_repeat[0], steps_to_repeat[1])
lcm2 = lcm(lcm1, steps_to_repeat[2])
print(lcm2)


