INPUT=348

list = [ 0 ]

pos = 0
for i in range(1, 50000000):
    pos = (pos + INPUT) % i
    if pos == 0:
        print(i)
    pos += 1

