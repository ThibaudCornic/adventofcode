def densify(mylist):
    xor = 0
    res = []
    for i in range(len(mylist)):
        if not i % 16:
            res.append(xor)
            xor = 0
        xor = xor ^ mylist[i]
    res.append(xor)
    return ''.join([ "{:02x}".format(i) for i in res[1:] ])

def hash(data, rounds=64):
    pos = 0
    skip_size = 0
    mylist = list(range(256))
    lengths = [ ord(x) for x in data ]
    lengths.extend([ 17, 31, 73, 47, 23 ])
    for j in range(rounds):
        for length in lengths:
            tmp_list = mylist.copy()
            for i in range(length):
                mylist[(pos + i) % len(mylist)] = tmp_list[(pos + length - 1 - i) % len(mylist) ]
            pos = (pos + length + skip_size) % len(mylist)
            skip_size += 1
    return densify(mylist)


def num_of_ones(string):
    total = 0
    for i in range(128):
        to_be_h = string + '-' + str(i)
        n = int(hash(to_be_h), 16)
        total += bin(n).count("1")
    return total

# test
print(num_of_ones("flqrgnkx"))
# part 1
print(num_of_ones("jxqlasbh"))

# part 2
def compute_grid(string):
    ones = []
    for i in range(128):
        to_be_h = string + '-' + str(i)
        n = int(hash(to_be_h), 16)
        ones.append("{0:0128b}".format(n))
    return ones

ones = compute_grid("jxqlasbh")


size = 128

def test_and_append(a1, b1, ones, l):
    if ones[a1][b1] == "1":
        l.add(a1*size+b1)

def neighbours(i, j, ones):
    l = set()
    if i > 0: test_and_append(i-1, j, ones, l)
    if j > 0: test_and_append(i, j-1, ones, l)
    if j < (size-1): test_and_append(i, j+1, ones, l)
    if i < (size-1): test_and_append(i+1, j, ones, l)
    return l

graph = {}
for i in range(size):
    for j in range(size):
        if ones[i][j] == "1":
            graph[(i*size+j)] = neighbours(i, j, ones)

def dfs(graph, visited, node):
    if visited is None:
        visited = set()
    group = { node }
    visited.add(node)
    for link in graph[node] - visited:
        group.update(dfs(graph, visited, link))
    return group

all_sets = []
visited = set()
number = 0
while len(visited) != len(graph):
    all_sets.append(dfs(graph, visited, list(graph.keys() - visited)[0]))
    number += 1

print(all_sets, number)
