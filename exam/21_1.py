def f21(list):
    i = 0
    if list[i] == "sqlpl":
        i = 1
        if (list[i] == 2004):
            i = 3
            if list[i] == 2020:
                return (0)
            if list[i] == 2003:
                return (1)
            if list[i] == 2014:
                return (2)
        if (list[i] == 1972):
            i = 3
            if list[i] == 2020:
                return (3)
            if list[i] == 2003:
                return (4)
            if list[i] == 2014:
                return (5)
    if list[i] == "jflex":
        i = 1
        if list[i] == 2004:
            i = 2
            if list[i] == 'j':
                return 6
            if list[i] == 'apl':
                return 7
            if list[i] == 'clean':
                return 8
        if list[i] == 1972:
                return 9
    if list[i] == "text":
        return (10)

print(f21(['jflex', 1972, 'apl', 2014]))
print(f21(['sqlpl', 1972, 'clean', 2014]))
