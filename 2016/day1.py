f = open("input1", "r")

north = lambda x, y: (x, y+1)
south = lambda x, y: (x, y-1)
east  = lambda x, y: (x+1, y)
west  = lambda x, y: (x-1, y)
d = 0
dirs = [ north, east, south, west ]
x, y = (0, 0)

hist = set()

for i in f.read().split(','):
    i = i.strip()
    if i[0] == "R":
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    for n in range(int(i[1:])):
        x, y = dirs[d](x, y)
        if (x, y) in hist:
            print(abs(x)+abs(y))
            exit()
        else:
            hist.add((x, y))

print(abs(x)+abs(y))
