r = str('Y')
num = list()
par = []  # Este é um outro jeito de criar listas abertas.
impar = list()
while r != 'N':
    n = int(input('Digite um número inteiro: '))
    num.append(n)
    r = 'Y'
    while r != 'S' and r != 'N':
        r = input('Você quer continuar? [S/N]: ').strip().upper()[0]
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os números digitados são: {num}')
print(f'Os números pares digitados são: {par}')
print(f'Os números ímpares digitados são: {impar}')
