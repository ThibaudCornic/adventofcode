f = open("input11", "r")

x = 0
y = 0

def steps(x, y):
    x = abs(x)
    y = abs(y)

    if x > y:
        steps = x
    else:
        steps = x
        steps += abs((y - x)/2)

    return steps

max_steps = 0
directions = f.read().strip().split(',')
for d in directions:
    s = steps(x, y)
    max_steps = max(s, max_steps)

    if d == 'n':
        y += 2
    if d == 'ne':
        x += 1
        y += 1
    if d == 'se':
        x += 1
        y -= 1
    if d == 's':
        y -= 2
    if d == 'sw':
        x -= 1
        y -= 1
    if d == 'nw':
        x -= 1
        y += 1

print("The moron is in ({}, {}), max_steps: {}".format(x, y, max_steps))


