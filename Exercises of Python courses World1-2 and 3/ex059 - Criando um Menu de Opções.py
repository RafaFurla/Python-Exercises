option = int(4)
while option != 5:
    if option == 4:
        n1 = int(input('Input a integer number: '))
        n2 = int(input('Input other integer number: '))
        s = int(n1 + n2)
        m = int(n1 * n2)
        if n1 >= n2:
            b = n1
        else:
            b = n2
    print('Choose one of the following options: ')
    option = int(input('''    [1] Add
    [2] Multiply
    [3] Bigger number
    [4] Put new values
    [5] Leave
    '''))
    if option == 1:
        print('{} + {} = {}'.format(n1, n2, s))
    elif option == 2:
        print('{} x {} = {}'.format(n1, n2, m))
    elif option == 3:
        print('{} > {}'.format(b, s - b))
    while option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
        print('Invalid option! Choose one of the following options: ')
        option = int(input('''        [1] Add
        [2] Multiply
        [3] Bigger number
        [4] Put new values
        [5] Leave
        '''))
print('End')
