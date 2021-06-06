from math import *

def f11(x):
    a1 = sqrt((pow(x,3) + pow(x, 8) / 26) / x**7 - cos(x))
    a2 = sqrt(log(x) + pow(x, 3) + 29)
    a3 = sqrt(67 * pow(x, 4) - sin(x))
    return (a1 + a2 + a3)

print(f11(91))
print(f11(49))
