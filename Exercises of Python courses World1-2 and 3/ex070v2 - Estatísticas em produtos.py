# Nome do programa
print('=' * 16)
print('CESTA DE COMPRAS')
print('=' * 16)
# Variáveis de entrada:
s = mp = float(0.00)
m1k = count = int(0)
nmp = str(' ')
# Início do programa
while True:
    n = str(input('Qual o nome do produto? ')).strip()
    p = float(input('Qual o preço do produto? R$ '))
    s += p
    count += 1
    if p > 1000.00:
        m1k += 1
    if count == 1 or p < mp:
        mp = p
        nmp = n
    while True:
        r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break
print('O total dispendido na compra foi de R$ {:.2f}'.format(s))
print(f'{m1k} produto(s) tem preço superior a mil reais!')
print('O produto mais barato é o/a {} que custa: R$ {:.2f}'.format(nmp, mp))
