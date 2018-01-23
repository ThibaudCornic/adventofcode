f = open("input21", "r")

import random

def flatten(obj):
    return '/'.join(obj)

def listify(obj):
    return obj.split('/')

def rotate(grid):
    obj = grid.split('/')
    size = len(obj)
    return flatten([ ''.join([ l[size-1-i] for l in obj ]) for i in range(size) ])

def flip(grid, horiz):
    obj = listify(grid)
    if horiz:
        for i in range(len(obj)):
            obj[i] = ''.join(reversed(obj[i]))
    else:
        obj.reverse()
    return flatten(obj)

rules = {}
for r in f:
    before, after = r.strip().split(" => ")
    after = listify(after)
    for i in range(4):
        rules[before] = after
        rules[flip(before, 1)] = after
        before = rotate(before)

init = listify(".#./..#/###")

def split_image(grid):
    size = len(grid)
    if size%2:
        chunk = 3
    else:
        chunk = 2

    r = []
    for i in range(0, size, chunk):
        for j in range(0, size, chunk):
            block = [ l[j:j+chunk] for l in grid[i:i+chunk] ]
            r.append(rules[flatten(block)])
    return (int(size/chunk), r)

def join_grid(blocks, blocks_per_line):
    size = len(blocks[0])
    r = []
    for i in range(blocks_per_line):
        line = zip(*blocks[i*blocks_per_line:(i+1)*blocks_per_line])
        r.extend([ "".join(l) for l in line])
    return r


def expand_img(image):
    blocks_per_line, blocks = split_image(image)
    return join_grid(blocks, blocks_per_line)

def print_img(image):
    print(image.replace('/', '\n'))
    print()

img = init
for i in range(18):
    img = expand_img(img)

print(sum([ i.count('#') for i in img]))
