lista = list()
r = str('Y')
while r != 'N':
    r = 'Y'
    lista.append(int(input('Digite um número inteiro: ')))
    while r != 'S' and r != 'N':
        r = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrescente ficam organizados da seguinte forma: {lista}')
lista.sort()
if lista.count(5) > 0:
    pos = list()
    for c, z in enumerate(lista):
        if z == 5:
            pos.append(c - 1)
    print('O número 5 aparece na lista! Na(s) posição(ões) {}'.format(pos))
else:
    print(f'O númro 5 não aparece na lista')
