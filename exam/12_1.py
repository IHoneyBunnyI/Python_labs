from math import *

def f12(x):
    if x < 157:
        return (x**2 - cos(x))
    elif 157 <= x < 221:
        return (65 * (28 * x**7 + 95* x**2)**8 - x**5)
    else:
        return (log(e**x - x**4 / 17 + 57) - abs(11 * x**2 - cos(x)))

print(f12(97))
print(f12(192))
