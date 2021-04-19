def swap(s):
    str1 = s[0]
    str2 = s[1]
    return s[-2] + s[-1] + s[2:-2] + str1 + str2

def f23(lis):
    b = []
    for sublist in lis:
        if sublist not in b:
            b.append(sublist)
    for i in range(len(b)):
        b[i].append('')
        b[i][2], b[i][1] = b[i][1].split('&')
    for i in range(len(b)):
        b[i][0] = b[i][0].split('[at]')[0]
    for i in range(len(b)):
        b[i][1] = b[i][1].replace('%', '')
        b[i][1] = str(float(b[i][1])/ 100)
    for i in range(len(b)):
        b[i][2] = b[i][2].replace('-', '.')
    for i in range(len(b)):
        b[i][2] = swap(b[i][2])
    return b
