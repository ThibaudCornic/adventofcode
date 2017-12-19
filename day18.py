from threading import Thread
import queue

f = open("input18", "r")

ins = []
for line in f:
    ins.append(line.strip().split())

def val(regs, c):
    if c in [ chr(x) for x in range(ord('a'), ord('a')+26) ]:
        return regs[ ord(c) - ord('a') ]
    else:
        return int(c)

last_freq = 0

fifos = [ queue.Queue(), queue.Queue() ]
blocked = [ False, False ]
sent = [ 0, 0 ]
finished = False

def execute(*a):
    last_printed = 0
    id = a[0]
    print("Starting thread", id)
    regs = [ 0 for i in range(26) ]
    regs[ord('p')-ord('a')] = id
    pc = 0
    while not finished:
        inst = ins[pc][0]
        args = ins[pc][1:]
        if inst == "set":
            regs[ord(args[0]) - ord('a')] = val(regs, args[1])
        if inst == "add":
            regs[ord(args[0]) - ord('a')] += val(regs, args[1])
        if inst == "mul":
            regs[ord(args[0]) - ord('a')] *= val(regs, args[1])
        if inst == "mod":
            regs[ord(args[0]) - ord('a')] %= val(regs, args[1])

        if inst == "snd":
            fifos[id^1].put(val(regs, args[0]))
            sent[id] += 1
            if id == 1 and sent[1] > last_printed+10:
                print(sent[1])
                last_printed = sent[1]

        if inst == "rcv":
            while fifos[id].empty():
                if finished:
                    return
                blocked[id] = True
            blocked[id] = False
            regs[ord(args[0]) - ord('a')] = fifos[id].get()
            fifos[id].task_done()

        if inst == "jgz":
            if val(regs, args[0]) > 0:
                pc += val(regs, args[1])
                continue
        pc += 1

t0 = Thread(target=execute, args=(0, ))
t1 = Thread(target=execute, args=(1, ))

t0.start()
t1.start()

while blocked != [ True, True ]:
    fifos[0].join()
    fifos[1].join()
    #print("Fifo0 empty")
    #print("Fifo1 empty")
    print(sent[1])
    pass

print("Finished", sent[1])
finished = True
exit()
