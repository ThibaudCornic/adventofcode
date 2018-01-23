chksum = 0

with open("input", "r") as f:
    for line in f.readlines():
        vals = [ int(t) for t in line.split('\t') ]
        _a = None
        _b = None
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                a = vals[i]
                b = vals[j]
                div = max(a,b) / min(a,b)
                if div.is_integer():
                    _a = int(max(a,b))
                    _b = int(min(a,b))
                    print("Choosing {} and {}: {}".format(_a, _b, _a/_b))
        chksum += _a/_b

print("Checksum:", chksum)
