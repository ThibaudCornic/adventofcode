f = open("input21", "r")

import random

def flatten(obj):
    return '/'.join([''.join(l) for l in obj])

def listify(obj):
    r = []
    for l in obj.split('/'):
        r.append([i for i in l])
    return r

def rotate(grid):
    obj = grid.split('/')
    size = len(obj)
    return flatten([ [ l[size-1-i] for l in obj ] for i in range(size) ])

def flip(grid, horiz):
    obj = listify(grid)
    if horiz:
        for i in obj:
            i.reverse()
    else:
        obj.reverse()
    return flatten(obj)

rules = {}
for r in f:
    a = r.split("=>")
    before = a[0].strip().replace('.', '0').replace('#', '1')
    after = listify(a[1].strip().replace('.', '0').replace('#', '1'))
    for i in range(4):
        rules[before] = after
        rules[flip(before, 1)] = after
        before = rotate(before)

init = "010/001/111"

def split_image(image):
    grid = listify(image)
    size = len(grid)
    if size%2:
        chunk = 3
    else:
        chunk = 2

    r = []
    for i in range(0, size, chunk):
        for j in range(0, size, chunk):
            r.append([ l[j:j+chunk] for l in grid[i:i+chunk] ])
    return (int(size/chunk), r)

def join_grid(blocks, blocks_per_line):
    size = len(blocks[0])
    x = 0
    y = 0
    r = [[] for i in range(size)]
    #print("Joining, size is {}, per line is {}, blocks {}".format(size,
    #    blocks_per_line, blocks))
    for b in blocks:
        for i in range(size):
            r[x+i].extend(b[i])
        y += 1
        if y == blocks_per_line and x < (blocks_per_line-1)*size:
            y = 0
            x += size
            r.extend([ [] for l in range(size)])
    return r


def expand_img(image):
    expanded = []
    blocks_per_line, blocks = split_image(image)
    
    for i in blocks:
        expanded.append(rules[flatten(i)])

    grid = join_grid(expanded, blocks_per_line)

    return flatten(grid)

def print_img(image):
    print(image.replace('/', '\n'))
    print()

img = init
for i in range(18):
    img = expand_img(img)

print(img.count('1'))
