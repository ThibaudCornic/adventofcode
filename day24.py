f = open("input24", "r")

blocks = []
for line in f:
    b = list(map(int, line.strip().split('/')))
    blocks.append(b)

def find_heaviest(start, blocks):
    possible = [ b for b in blocks if start in b ]
    weight = 0
    for b in possible:
        blocks_n = blocks.copy()
        blocks_n.remove(b)
        n = b[b.index(start) - 1]
        weight = max(weight, sum(b) + find_heaviest(n, blocks_n))
    return weight

def find_longest(start, blocks):
    possible = [ b for b in blocks if start in b ]
    weight = 0
    length = 0
    for b in possible:
        blocks_n = blocks.copy()
        blocks_n.remove(b)
        n = b[b.index(start) - 1]
        l, w = find_longest(n, blocks_n)
        if l+1 >= length:
            w += sum(b)
            if l+1 == length:
                weight = max(weight, w)
            else:
                weight = w
            length = l+1
    return (length, weight)

print(find_heaviest(0, blocks))
print(find_longest(0, blocks)[1])
