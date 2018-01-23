test="0 2 7 0"
input6="11  11  13  7   0   15  5   5   4   4   1   1   7   1   15  11"


banks = input6.split()

print(banks)

def realloc(string):
    memory = [ int(x) for x in string.split(',')]
    i = memory.index(max(memory))
    val = memory[i]
    memory[i] = 0
    for j in range(val):
        i = i + 1
        if i == len(memory):
            i = 0
        memory[i] += 1
    return ','.join([str(x) for x in memory])

all_vals = {}
banks = ','.join(banks)
all_vals[banks] = 0
steps = 1
banks = realloc(banks)
while banks not in all_vals.keys():
    all_vals[banks] = steps
    banks = realloc(banks)
    steps += 1

print(steps - all_vals[banks])
