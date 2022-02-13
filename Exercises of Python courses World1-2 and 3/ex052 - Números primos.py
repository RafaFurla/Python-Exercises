n = int(input('Digite um número inteiro: '))
t = int(0)
for c in range(1, n+1, 1):
    if (n / c) == (n // c):
        t = t + 1
if t == 2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} não é primo!'.format(n))
