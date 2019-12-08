
WIDTH = 25
HEIGHT = 6
BLACK = '0'
WHITE = '1'
TRANSPARENT = '2'
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

total_layers = len(layers)
layer_len = len(layers[0])
final_picture = []
for pixel in range(0, layer_len):
    for layer in range(0, total_layers):
        if layers[layer][pixel] == TRANSPARENT:
            continue
        else:
            final_picture.append(int(layers[layer][pixel]))
            break


final_picture_str = ""
j = 0
white = u"\u2588"
black = " "
for i in range(0, layer_len):
    if final_picture[i]:
        final_picture_str += white
    else:
        final_picture_str += black
    j += 1
    if j == WIDTH:
        final_picture_str += "\n"
        j = 0

print(final_picture_str)

