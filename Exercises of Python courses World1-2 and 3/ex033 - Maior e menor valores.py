# Lê 3 números e diz qual o maior e qual o menor
n1 = int(input('Digite 3 números inteiros (aperte enter entre eles): '))
n2 = int(input('                                                   : '))
n3 = int(input('                                                   : '))
if n1 > n2:
    if n1 > n3:
        print('{} é o maior número digitado!'.format(n1))
        if n2 > n3:
            print('{} é o menor número digitado!'.format(n3))
        else:
            print('{} é o menor número digitado!'.format(n2))
if n2 > n1:
    if n2 > n3:
        print('{} é o maior número digitado!'.format(n2))
        if n1 > n3:
            print('{} é o menor número digitado!'.format(n3))
        else:
            print('{} é o menor número digitado!'.format(n1))
if n3 > n1:
    if n3 > n2:
        print('{} é o maior número digitado!'.format(n3))
        if n1 > n2:
            print('{} é o menor número digitado!'.format(n2))
        else:
            print('{} é o menor número digitado!'.format(n1))
if n1 == n2 == n3:
    print('Os 3 números são iguais!')
