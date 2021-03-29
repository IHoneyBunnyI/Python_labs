def f21(list):
    i = 0
    if list[i] == 1988:
        i = 3
        if list[i] == 2018:
            i = 2
            if list[i] == 1977:
                return 0
            elif list[i] == 1978:
                return 1
        elif list[i] == 2020:
            i = 1
            if list[i] == 1976:
                return 2
            elif list[i] == 1974:
                return 3
        elif list[i] == 2008:
            i = 2
            if list[i] == 1977:
                return 4
            elif list[i] == 1978:
                return 5
    elif list[i] == 1982:
        i = 3
        if list[i] == 2018:
            return 6
        elif list[i] == 2020:
            i = 2
            if list[i] == 1977:
                return 7
            elif list[i] == 1978:
                return 8
        elif list[i] == 2008:
            return 9
