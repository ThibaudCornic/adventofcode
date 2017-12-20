INPUT=348

list = [ 0 ]

pos = 0
for i in range(1, 2018):
    pos = (pos + INPUT) % i
    list.insert(pos + 1, i)
    pos += 1

print(list[pos-5:pos+5])
print(list[(pos+1) % 2018])

