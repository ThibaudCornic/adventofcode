f = open("input25", "r")

curstate = f.readline().strip()[-2]
steps = int(f.readline().strip().split(" ")[-2])
tmp = f.readline()

states = {}
state = ''

line = f.readline()
while line:
    state = line.strip()[-2]
    actions = []
    for i in range(2):
        tmp = f.readline()
        val = int(f.readline().strip()[-2])
        move = 1 if f.readline().strip().split(" ")[-1] == "right." else -1
        next_state = f.readline().strip()[-2]
        actions.append((val, move, next_state))
    tmp = f.readline()
    states[state] = actions
    line = f.readline()


ones = set()
index = 0
print(states)
state = curstate

for step in range(steps):
    val, move, next_state = states[state][1] if index in ones else states[state][0]
    if val:
        ones.add(index)
    else:
        if index in ones:
            ones.remove(index)
    index += move
    state = next_state
    #print("After {} steps: idx {}, state {}, ones {}".format(step+1, index, state, ones))

print(len(ones))

