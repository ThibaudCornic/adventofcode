f = open("input22", "r")

infected = set()
weakened = set()
flagged = set()
off = 0
for l in f:
    if off == 0:
        off = -1 * int((len(l.strip()) - 1) / 2)
        y = off
        x = 0
        print(off, x, y)
    for i,e in enumerate(l.strip()):
        if e == '#':
            infected.add((i+off,y))
    y += 1

up    = lambda x,y: (x, y-1)
down  = lambda x,y: (x, y+1)
right = lambda x,y: (x+1, y)
left  = lambda x,y: (x-1, y)

direcs = [ up, right, down, left ]
direc = 0
bad = 0
def burst(x, y, direc, infected):
    global bad
    if (x,y) in weakened:
        infected.add((x,y))
        weakened.remove((x,y))
        bad += 1
    elif (x,y) in infected:
        direc = (direc+1) % 4
        infected.remove((x,y))
        flagged.add((x,y))
    elif (x,y) in flagged:
        direc = (direc+2) % 4
        flagged.remove((x,y))
    else:
        direc = (direc-1) % 4
        weakened.add((x,y))
    x, y = direcs[direc](x, y)
    return (x, y, direc, infected)



x = 0
y = 0
for i in range(10000000):
    x, y, direc, infected = burst(x, y, direc, infected)


print(bad)
