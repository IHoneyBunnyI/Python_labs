from math import *

def f14(x):
    if x == 0:
        return 3
    else:
        return (sin(f14(x - 1)) - 1/16*(f14(x - 1)**3))
print(f14(8))
print(f14(9))
