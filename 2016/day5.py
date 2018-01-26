#!/usr/bin/python3
import sys
from hashlib import md5

if __name__ == "__main__":
    input = bytearray("abc", "utf-8")
    if len(sys.argv) > 1:
        input = bytearray(sys.argv[1], "utf-8")

password1 = ""
password2 = ["_"] * 8

i = 0
while "_" in password2: # The part1 is always faster to complete
    hash = md5(input+bytearray([ord(l) for l in str(i)])).hexdigest()
    if hash.startswith("00000"):
        # part 1
        if len(password1) < 8:
            password1 += hash[5]

        # part 2
        idx = int(hash[5], 16)
        if idx < 8:
            if password2[idx] == "_":
                password2[idx] = hash[6]

    i += 1
    # log every million try
    if not i % (1024*1024):
        print(i, "".join(password2), password1, end='\r')

print()
print("Finished:", password1, "".join(password2))
