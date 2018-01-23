with open("input5", "r") as f:
    inst = []
    size = 0
    for i in f.readlines():
        inst.append(int(i.split()[0]))
        size += 1
    
    index = 0
    steps = 0
    while index < size and index >= 0:
        increment = inst[index]
        if increment >= 3:
            inst[index] -= 1
        else:
            inst[index] += 1

        index += increment
        steps += 1

    print(steps)
