
up    = lambda x, y, pad: (x, y-1) if pad[y-1][x] != " " else (x, y)
down  = lambda x, y, pad: (x, y+1) if pad[y+1][x] != " " else (x, y)
left  = lambda x, y, pad: (x-1, y) if pad[y][x-1] != " " else (x, y)
right = lambda x, y, pad: (x+1, y) if pad[y][x+1] != " " else (x, y)
moves = {
        "U": up,
        "D": down,
        "L": left,
        "R": right
        }

keypad2 = [
"       ",
"   1   ",
"  234  ",
" 56789 ",
"  ABC  ",
"   D   ",
"       ",
]

keypad1 = [
"     ",
" 123 ",
" 456 ",
" 789 ",
"     ",
] 


with open("input2", "r") as f:
    code = ""
    x, y = (2, 2)
    for l in f:
        l = l.strip()
        for d in l:
            (x, y) = moves[d](x, y, keypad1)
        code += keypad1[y][x]
    print(code)

with open("input2", "r") as f:
    code = ""
    x, y = (1, 3)
    for l in f:
        l = l.strip()
        for d in l:
            (x, y) = moves[d](x, y, keypad2)
        code += keypad2[y][x]
    print(code)
