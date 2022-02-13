# O programa lê um número e diz se ele é par ou ímpar
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))
