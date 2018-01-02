b = 106500
c = b + 17000

from math import sqrt

# This function has been taken from https://www.codecademy.com/en/forum_questions/5089b82e0c55f002000018ed
def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

h = 0

for n in range(b, b + 17017, 17):
    if not is_prime(n):
        h += 1

print(h)

