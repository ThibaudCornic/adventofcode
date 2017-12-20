import string

f = open("input19", "r")

graph = []

for line in f:
    graph.append(line)

start = graph[0].index('|')

x = start
y = 0
result = ""
steps = 0
dir = 3 # down

def print_grid(x, y):
    for i in range(len(graph)):
        if i == y:
            _line = graph[y][:x] + 'X' + graph[y][x+1:]
            print(_line)
            continue
        print(graph[i])


def one_step(x, y, dir):
    if dir == 0:
        return (x+1, y)
    if dir == 1:
        return (x, y-1)
    if dir == 2:
        return (x-1, y)
    if dir == 3:
        return (x, y+1)
    raise Exception("Wrong direction", dir)

def turn(x, y, dir):
    if dir != 2:
        if graph[y][x+1] in '-'+string.ascii_letters:
            return 0
    if dir != 3:
        if graph[y-1][x] in '|'+string.ascii_letters:
            return 1
    if dir != 0:
        if graph[y][x-1] in '-'+string.ascii_letters:
            return 2
    if dir != 1:
        if graph[y+1][x] in '|'+string.ascii_letters:
            return 3
    raise Exception("Can't turn")

while graph[y][x] != ' ':
    if graph[y][x] in string.ascii_letters:
        result += graph[y][x]
    if graph[y][x] == '+':
        dir = turn(x, y, dir)
    a = one_step(x, y, dir)
    steps += 1
    x = a[0]
    y = a[1]


print(x, y)
print(result)
print("{} steps".format(steps))
