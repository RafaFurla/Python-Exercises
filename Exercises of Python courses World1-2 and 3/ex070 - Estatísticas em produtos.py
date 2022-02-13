# Nome do programa
print('=' * 16)
print('CESTA DE COMPRAS')
print('=' * 16)
# Variáveis de entrada:
s = float(0.00)
m1k = int(0)
r = str('Y')
# Início do programa
n = str(input('Qual o nome do produto? ')).strip()
p = float(input('Qual o preço do produto? R$ '))
s += p
nmp = n
mp = p
if p > 1000.00:
    m1k += 1
# Início da estrutura de repetição
while r != 'S' and r != 'N':
    r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
while r == 'S':
    n = str(input('Qual o nome do produto? ')).strip()
    p = float(input('Qual o preço do produto? R$ '))
    s += p
    if p > 1000.00:
        m1k += 1
    if p < mp:
        mp = p
        nmp = n
    while True:
        r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if r == 'S':
            break
        elif r == 'N':
            break
print('O total dispendido na compra foi de R$ {:.2f}'.format(s))
print(f'{m1k} produto(s) tem preço superior a mil reais!')
print('O produto mais barato é o/a {} que custa: R$ {:.2f}'.format(nmp, mp))
