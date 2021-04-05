def f23(lis):
    l = [[row[i] for row in lis] for i in range(len(lis[0]))]
    b = []
    for sublist in l:
        if sublist not in b:
            b.append(sublist)
    new = []
    for i in range(len(b[1])):
        liststr = list(b[1][i])
        tmp, tmp2 = liststr[0], liststr[1]
        liststr[0], liststr[1] = liststr[-2], liststr[-1]
        liststr[-2], liststr[-1] = tmp, tmp2
        stroka = ''.join(liststr)
        b[1].remove(b[1][i])
        b[1].insert(i, stroka)
    return b

        


lis = [["Да", "00-06-07", "+7 076 160‐84‐04", "Да", "Альберт Д. Сакин", "00-06-07"],
        ["Да", "99‐08‐09", "+7 577 383‐22‐87", "Да", "Ростислав Е. Воруфич", "99‐08‐09"],
        ["Да", "99‐06‐22", "+7 720 893‐17‐03", "Да", "Олег У. Вишман", "99‐06‐22"]]
a = [[1, 1, 3, 3, 3],
     [2, 2, 4, 4, 4],
     [3, 3, 5, 5, 5]] 
print(f23(lis))
