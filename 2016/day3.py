#!/usr/bin/python3
import sys

if __name__ == "__main__":
    fname = "input3"
    if len(sys.argv) > 1:
        fname = sys.argv[1]

def is_possible(sides):
    s = sorted(sides)
    return 1 if s[0] + s[1] > s[2] else 0


possible_row = 0
possible_col = 0

triangles = [ [] for i in range(3) ]

with open(fname, "r") as f:
    i = 0
    for l in f:
        triangles[i] = list(map(int, l.split()))
        if i == 2:
            i = 0
            possible_row += sum(map(is_possible, triangles))
            possible_col += sum(map(is_possible, zip(*triangles)))
        else:
            i+= 1

print("Possible rows:", possible_row)
print("Possible cols:", possible_col)
