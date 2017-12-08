f = open("input8", "r")

regs = {}
maximum = 0
for i in f.readlines():
    words = i.split()
    r0 = words[0]
    mult = 1 if words[1] == "inc" else -1
    increment = int(words[2])
    cond0 = words[4]
    comparison = words[5]
    cond1 = int(words[6])

    if not r0 in regs.keys():
        regs[r0] = 0
    if not cond0 in regs.keys():
        regs[cond0] = 0

    comp_str = "{} {} {}".format(regs[cond0], comparison, cond1)
    if eval(comp_str):
        regs[r0] += mult * increment
        if regs[r0] > maximum:
            maximum = regs[r0]

print(max(regs.values()))
print(maximum)


