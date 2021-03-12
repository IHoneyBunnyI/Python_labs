from math import *

def f12(x):
    if (x < 20):
        res = pow((pow(x, 4) + sin(x) + 70), 5) - x
    elif (20 <= x < 92):
        res = fabs(pow(x, 3)/56) + 95 * pow(x , 2)
    else:
        res = 8 * pow(x, 8) - 4 * pow(x, 4)
    return (res)
