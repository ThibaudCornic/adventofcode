f = open("input13", "r")


scanners = [ [ int(v) for v in line.split(':') ] for line in f ]

def cost_with_start(start):
    cost = 0
    hits = 0
    for a in scanners:
        depth = a[0]
        r = a[1]
        caught = (depth + start) % (2 * r - 2) == 0
        if caught == 1:
            cost += depth * r
            hits += 1
    return (cost, hits)

print(cost_with_start(0)[0])
start = 0
while cost_with_start(start)[1] != 0:
    start += 1

print("Lowest is {}: {}".format(start, cost_with_start(start)))
