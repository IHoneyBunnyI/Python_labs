from math import *

def f(x, y):
    res = sqrt(tan(pow(x, 4)) + pow(x, 7)) + ((22*pow(x,3)) + (14*pow(x, 4)) - 98)/\
            (pow(y, 3) + 82 * pow(y, 6)) + (30 * pow(x, 8) + 35 * pow(x, 4)) /\
            (16* pow(x, 4) + x)
    print (res)
    

def f2(x):
    if (x < 20):
        res = pow((pow(x, 4) + sin(x) + 70), 5) - x
    elif (20 <= x < 92):
        res = fabs(pow(x, 3)/56) + 95 * pow(x , 2)
    else:
        res = 8 * pow(x, 8) - 4 * pow(x, 4)
    print (res)

def f3(n, m):
    tmp1 = 0;
    tmp2 =0;
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            tmp1 += ((pow(j, 6)) - (15 * pow(j, 3)))
    for k in range(1, n + 1):
        tmp2 += (log(k, e) + log(k, e))
    res = 12 * tmp1 + 14 * tmp2
    print(res)

def f4(n):
    if n == 0:
        return 10
    if n == 1:
        return 9
    return (sin(f4(n - 1)) + (1/36) * f4(n -2))
    
def main():
    f(59, -69)
    f(21, -93)
    f2(-5)
    f2(140)
    f3(63, 83)
    f3(92, 42)
    print(f4(4))
    print(f4(13))

if __name__ == "__main__":
    main()
