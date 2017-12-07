number=361527

def steps(number):
    found = False
    square=1
    while not found:
        if number <= square**2:
            diff_above = square**2 - number
            diff_below = number - (square-2)**2
            #print("For {}, square is {}, {} from below, {} from above".format(number, square, diff_below, diff_above))
            # Opposite to square ** 2
            if diff_above == diff_below:
                return square-1

            # Closer to square
            if diff_above < diff_below:
                corner = square ** 2
                if diff_above < square:
                    return (square - 1)/2 + abs(number - (corner - (square - 1)/2))
                else:
                    return (square - 1)/2 + abs(number - (corner - ((square - 1) * 3)/2))
            else:
                corner = (square - 2) ** 2
                if diff_below < square:
                    return (square - 1)/2 + abs(number - (corner + (square - 1)/2))
                else:
                    return (square - 1)/2 + abs(number - (corner + ((square - 1) * 3)/2))
        square += 2

width = int(steps(361527))


big = [ [ 0 for i in range(width) ] for j in range(width) ]

def compute(x,y):
    val = 0
    for i in range(-1, 2):
        val += big[x+1][y+i]
        val += big[x-1][y+i]
    val += big[x][y+1]
    val += big[x][y-1]
    if val > number:
        print("({},{}) = {}".format(x, y, val))
    return val

big[0][0] = 1
x=0
y=0
step=1
while(big[x][y] < number):
    x+=1
    for i in range(step):
        big[x][y] = compute(x,y)
        y+=1
    for i in range(step+1):
        big[x][y] = compute(x,y)
        x-=1
    for i in range(step+1):
        big[x][y] = compute(x,y)
        y-=1
    for i in range(step+1):
        big[x][y] = compute(x,y)
        x+=1
    big[x][y] = compute(x,y)
    step+=2


