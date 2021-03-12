from math import *

def f13(n, m):
    tmp1 = 0;
    tmp2 =0;
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            tmp1 += ((pow(j, 6)) - (15 * pow(j, 3)))
    for k in range(1, n + 1):
        tmp2 += (log(k, e) + log(k, e))
    res = 12 * tmp1 + 14 * tmp2
    return (res)
