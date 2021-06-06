from math import *

def f13(n, m):
    a = 0
    b = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a += 17 * j**5 - j**7 + 24
    for i in range(1, n + 1):
        b += 45 * i**8 + i**5
    return (75 * a + 8 * b)

print(f13(28, 59))
print(f13(60, 43))
