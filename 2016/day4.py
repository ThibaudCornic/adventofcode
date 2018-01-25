#!/usr/bin/python3
import sys
import re
from collections import Counter
from operator import itemgetter


if __name__ == "__main__":
    fname = "input4"
    if len(sys.argv) > 1:
        fname = sys.argv[1]

def rotate(letter, n):
    c = ord(letter) - ord('a')
    c = (c + n) % 26
    return chr(c + ord('a'))

with open(fname, "r") as f:
    result = 0
    for line in f:
        m = re.match(r'([a-z-]+)([0-9]+)\[([a-z]+)\]', line)
        name, ID, cksum = m.groups()
        ID = int(ID)

        ### Part 1
        # Count the number of occurrences of each letter
        letters = Counter(name.replace("-", "")).most_common()

        # sort is stable => sort by keys first, and the keys order will be
        # preserved when sorting by numbers
        letters.sort(key=itemgetter(0))
        letters.sort(key=itemgetter(1), reverse=True)
        
        # Get the first five and test the cksum
        test_chksum = "".join([ letters[i][0] for i in range(5) ])
        if test_chksum == cksum:
            result += ID

        ### Part 2
        text = "".join([ rotate(l, ID) if l is not " " else l for l in name ])
        if "north" in text:
            print(text, ID)

    print(result)
