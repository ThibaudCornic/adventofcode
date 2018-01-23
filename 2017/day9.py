f = open("input9", "r")
#f = open("test9", "r")


open_groups = 0
groups = 0
total_score = 0

i = 0

def parse_group(stream, depth):
    garbage = False
    score = 0
    i = 0
    while i < len(stream):
        c = stream[i]
        i += 1
        if garbage:
            if c == '>':
                garbage = False
            if c == '!':
                i += 1
            continue

        if c == '<':
            garbage = True
        if c == '{':
            (s, end) = parse_group(stream[i:], depth+1)
            score += s
            i += end
        if c == '}':
            return (score + depth, i)
    return (score, i)

def count_garbage(stream):
    garbage = False
    score = 0
    i = 0
    while i < len(stream):
        c = stream[i]
        i += 1
        if garbage:
            if c == '>':
                garbage = False
            elif c == '!':
                i += 1
            else:
                score += 1
            continue

        if c == '<':
            garbage = True
        if c == '{':
            (s, end) = count_garbage(stream[i:])
            score += s
            i += end
        if c == '}':
            return (score, i)
    return (score, i)

for stream in f.readlines():
    stream = stream[:len(stream)-1]
    print("Processing stream '{}'".format(stream))
    print("\t(total_score, end) =", parse_group(stream, 0))
    print("\t(garbage, end) =", count_garbage(stream))
