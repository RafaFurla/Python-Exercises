soma = int(0)
t = int(0)
for c in range(3, 501, 3):
    if c % 2 == 1:
        soma = soma + c
        t = t + 1
print('A soma de todos os {} números ímpares e múltiplos de 3 entre 1 e 500 é igual a {}!'.format(t, soma))
