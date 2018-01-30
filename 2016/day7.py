#!/usr/bin/python3
import sys
import re

if __name__ == "__main__":
    fname = "input7"
    if len(sys.argv) > 1:
        fname = sys.argv[1]

def contains_abba(s):
    for i,c in enumerate(s):
        if i+3 < len(s):
            if s[i+1] != c and s[i+3] == c and s[i+2] == s[i+1]:
                return True
    return False

def contains_aba(s, line):
    in_brackets = False
    for i,c in enumerate(s):
        if i+2 < len(s):
            b = s[i+1]
            if b != '[' and b != c and s[i+2] == c:
                if re.search(r"\[[a-z]*"+b+c+b, line):
                    return True

with open(fname, "r") as f:
    abba = 0
    aba = 0
    for line in f:
        # part 1
        m = re.findall(r'\[([a-z]*)\]', line)
        if not True in map(contains_abba, m):
            m = re.split(r'\[[a-z]*\]', line)
            if True in map(contains_abba, m):
                abba += 1

        # part 2
        m = re.split(r'\[[a-z]*\]', line)
        if True in [ contains_aba(s, line) for s in m ]:
            aba += 1

print(abba)
print(aba)
