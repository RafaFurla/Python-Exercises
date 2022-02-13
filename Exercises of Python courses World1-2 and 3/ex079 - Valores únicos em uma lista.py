num = list()
r = str('Y')
'''c = int(-1)
while not r == 'N':
    c += 1
    if c == 0:
        num.append(int(input('Digite um número inteiro: ')))
        print('Valor adicionado com sucesso!')
    else:
        while True:
            p = int(input('Digite um outro número inteiro: '))
            if num.count(p) == 0:
                num.append(int(p))
                print('Valor adicionado com sucesso...')
                break
            else:
                print(f'{p} já foi digitado antes! Não vou adicionar...')
    while True:
        r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
print(f'Os números digitados em ordem crescente são: {sorted(num)}')'''
while r != 'N':
    n = int(input('Digite um número inteiro: '))
    if n not in num:
        num.append(n)
        print('O número foi adicionado com sucesso...')
    else:
        print('O número já foi digitado! Não vou adicionar...')
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
print(f'Os números digitados em ordem crescente são: {sorted(num)}')
