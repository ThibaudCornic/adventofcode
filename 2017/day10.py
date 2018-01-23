def circ_list_reverse(l, start, end):
    _size = len(l)
    if end <= start:
        to_rev = l[start:] + l[:end]
        to_rev.reverse()
        return to_rev[_size-start:] + l[end:start] + to_rev[:_size-start]
    else:
        to_rev = l[start:end]
        to_rev.reverse()
        return l[:start] + to_rev + l[end:]

def one_round(mylist, pos, skip_size, lengths):
    size = len(mylist)
    i = pos
    for length in lengths:
        if length:
            mylist = circ_list_reverse(mylist, i, (i + length) % size)
        i = (i + length + skip_size) % size
        skip_size += 1
    return (mylist, i, skip_size)

def data_to_lengths(data):
    return [ ord(x) for x in data ] + [ 17, 31, 73, 47, 23 ]


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
    mylist = [ i for i in range(256) ]
    lengths = data_to_lengths(data)
    for i in range(rounds):
        (mylist, pos, skip_size) = one_round(mylist, pos, skip_size, lengths)
    return densify(mylist)


# test 1
f = open("input10", "r")
#f = open("test10", "r")
#lengths = [ int(x) for x in f.read().split(',') ]
#a = one_round([ 0 for i in range(256)], 0, 0, lengths)[0]
#print(a[0]*a[1])

test = [ "", "AoC 2017", "1,2,3", "1,2,4" ]
for i in test:
    print(hash(i))
print(hash(f.read().strip()))
