import re
from itertools import combinations
from copy import deepcopy

f = open('12_puzzle_input.txt', 'r')
lines = f.readlines()

STEPS = 1000
NUM_MOONS = 4
position = {}
velocity = {}
index = 0
for line in lines:
    axes = re.split("<x=(.+), y=(.+), z=(.+)>", line)
    position[index] = [int(axes[1]), int(axes[2]), int(axes[3])]
    velocity[index] = [0, 0, 0]
    index += 1


def apply_gravity(moon_a, moon_b):
    for i in range(0, 3):
        if position[moon_a][i] > position[moon_b][i]:
            velocity[moon_a][i] -= 1
            velocity[moon_b][i] += 1
        elif position[moon_a][i] < position[moon_b][i]:
            velocity[moon_a][i] += 1
            velocity[moon_b][i] -= 1


def apply_velocity(moon):
    for i in range(0, 3):
        position[moon][i] += velocity[moon][i]


def potential_energy(moon):
    return abs(position[moon][0]) + abs(position[moon][1]) + abs(position[moon][2])


def kinetic_energy(moon):
    return abs(velocity[moon][0]) + abs(velocity[moon][1]) + abs(velocity[moon][2])


def total_energy():
    energy = 0
    for n in range(0, NUM_MOONS):
        energy += potential_energy(n) * kinetic_energy(n)
    return energy


moon_combos = list(combinations(position.keys(), 2))
for s in range(0, STEPS):
    for c in range(0, len(moon_combos)):
        apply_gravity(moon_combos[c][0], moon_combos[c][1])

    for m in range(0, NUM_MOONS):
        apply_velocity(m)

print(total_energy())