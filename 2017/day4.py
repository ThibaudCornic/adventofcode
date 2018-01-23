res = 0

with open("input4", "r") as f:
    for line in f.readlines():
        d={}
        words = line.split()
        letters = [ [ a for a in w] for w in words ]
        for w in letters:
            w.sort()
        print(letters)
        dup = [ x for x in letters if letters.count(x) > 1 ]
        if dup == []:
            res += 1

print(res)
