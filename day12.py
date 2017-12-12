import re

#f = open("test12", "r")
f = open("input12", "r")

def add_to_group(group, pipes):
    for pipe in pipes:
        group.add(pipe)


groups = []
for line in f.readlines():
    m = re.match(r"([0-9]*) <-> ([0-9, ]*)$", line)
    prog = int(m.group(1))
    pipes = { int(x) for x in m.group(2).strip().split(',') }
    pipes.add(prog)

    belonging_to = [ i for i in range(len(groups)) if pipes & groups[i] != set() ]
    if len(belonging_to):
        first = belonging_to[0]
        groups[first].update(pipes)
        for i in belonging_to[1:]:
            groups[first].update(groups[i])
            groups[i] = set()
    else:
        print("Creating new set for", pipes)
        groups.append( pipes )


# Sanity check...
for i in range(len(groups)):
    for j in range(i+1, len(groups)):
        if groups[i] & groups[j]:
                raise Exception("Collision in {} {}".format(i,j))

groups = list(filter(lambda x: x != set(), groups))
print(len([ g for g in groups if 0 in g ][0]))
print(len(groups))

