import re
import itertools
import operator

#f = open("test20", "r")
f = open("input20", "r")


parts = []

for line in f:
    m = re.findall(r'[0-9-]+', line)
    parts.append( { 'p': tuple(map(int, m[:3])), 'v': tuple(map(int, m[3:6])), 'a': tuple(map(int, m[6:]) )} )

abs_acc = [ sum(l) for l in [ map(abs, acc) for acc in [ part['a']  for part in parts ] ] ]
print(abs_acc.index(min(abs_acc)))


for i in range(1000):
    for part in parts:
        part['v'] = tuple(map(lambda x : x[0]+x[1], zip(part['v'], part['a'])))
        part['p'] = tuple(map(lambda x : x[0]+x[1], zip(part['p'], part['v'])))
    parts.sort(key = lambda x: x['p'])

    # remove n-plicates
    j = 0
    while j < len(parts):
        k = j+1
        while k < len(parts) and parts[j]['p'] == parts[k]['p']:
            k += 1
        if k == j+1:
            j += 1
        else:
            parts[j:k] = []

    # print remaining elems
    if not i % 100: print(len(parts), i)
