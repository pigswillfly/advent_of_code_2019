
WIDTH = 25
HEIGHT = 6

f = open('8_puzzle_input.txt', 'r')

layers = []
i = 0
next_layer = True
width = 0
height = 0

next_char = f.read(1)
while next_char:
    if next_layer:
        next_layer = False
        layers.append([])
    layers[i].append(next_char)
    width += 1
    if width == WIDTH:
        width = 0
        height += 1
    if height == HEIGHT:
        height = 0
        next_layer = True
        i += 1
    next_char = f.read(1)

layer_counts = []
for layer in range(0, len(layers)):
    layer_counts.append(0)
    for ch in layers[layer]:
        if ch == '0':
            layer_counts[layer] += 1

min_zeroes_layer = layer_counts.index(min(layer_counts))
twos = 0
ones = 0
for ch in layers[min_zeroes_layer]:
    if ch == '2':
        twos += 1
    elif ch == '1':
        ones += 1

print(twos * ones)
