from collections import deque

f = open("input16", "r")
#f = open("test16", "r")

ins = []
for i in f.read().strip().split(','):
    if i[0] == 's':
        ins.append( (0, int(i[1:])) )
    if i[0] == 'x':
        j, k = (int(x) for x in i[1:].split('/'))
        ins.append( (1, j, k) )
    if i[0] == 'p':
        j, k = i[1:].split('/')
        ins.append( (2, j, k) )

#progs = "abcdefghijklmnop"
progs = [ chr(ord('a') + i) for i in range(16) ]
start = 0
#progs = deque([range(16)])

for j in range(1000000000 % 112):
    if j and progs == [ chr(ord('a') + i) for i in range(16) ]:
        print(j)
        exit()
    for i in ins:
        if i[0] == 0:
            start = (start - i[1]) % 16
        if i[0] == 1:
            j = i[1]
            k = i[2]
            j = (j + start) % 16
            k = (k + start) % 16
            tmp = progs[j]
            progs[j] = progs[k]
            progs[k] = tmp
        if i[0] == 2:
            j = progs.index(i[1])
            k = progs.index(i[2])
            tmp = progs[j]
            progs[j] = progs[k]
            progs[k] = tmp

        
print(''.join([ progs[(i+start)%16] for i in range(16) ]))
