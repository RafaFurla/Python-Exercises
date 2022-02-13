print('=' * 40)
print('{:^40}'.format('MAIOR E MENOR NA LISTA'))
print('=' * 40)
n = list()
posmax = list()
posmin = list()
for c in range(0, 5):
    n.append(int(input('Entre com um número inteiro: ')))
for k, c in enumerate(n):
    if max(n) == c:
        posmax.append(int(k))
    if min(n) == c:
        posmin.append(int(k))
print(f'Os valores digitados foram: {n}')
print(f'O maior valor digitado foi o {max(n)} e está na(s) posição(ões) ', end='')
for p in posmax:
    print(f'{p}...', end=' ')
print('da lista!')
print(f'O menor valor digitado foi o {min(n)} e está na(s) posição(ões) ', end='')
for o in posmin:
    print(f'{o}...', end=' ')
print('da lista!')
