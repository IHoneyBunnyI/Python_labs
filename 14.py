from math import *

def f4(n):
    if n == 0:
        return 10
    if n == 1:
        return 9
    return (sin(f4(n - 1)) + (1/36) * f4(n -2))
