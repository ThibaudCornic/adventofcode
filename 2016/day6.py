#!/usr/bin/python3
import sys
from collections import Counter


if __name__ == "__main__":
    fname = "input6"
    if len(sys.argv) > 1:
        fname = sys.argv[1]


with open(fname, "r") as f:
    message = [ l.strip() for l in f.readlines() ]

    # most common letter of each column
    part1 = [ l.most_common(1)[0][0] for l in map(Counter, zip(*message)) ]
    print("".join(part1))

    # least frequent letter of each column
    part2 = [ l.most_common()[-1][0] for l in map(Counter, zip(*message)) ]
    print("".join(part2))
