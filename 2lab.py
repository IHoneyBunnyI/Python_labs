#BONUS QUINE :D
s='s=%r;print(s%%s)';print(s%s)
print('\n')

def tree_design(list):
    i = 2
    if list[i] == 2006:
        i = 1
        if list[i] == 'shell':
            return 0
        elif list[i] == 'urweb':
            return 1
        elif list[i] == 'ruby':
            return 2
    elif list[i] == 1971:
        i = 0
        if list[i] == 1992:
            return 3
        elif list[i] == 1967:
            return 4
        elif list[i] == 1972:
            return 5


def main():
    print(tree_design([1992, 'shell', 2006]))
    print(tree_design([1967, 'urweb', 2006]))



if __name__ == "__main__":
    main()
