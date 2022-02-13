n = (int(input('Digite um número inteiro: ')),
     int(input('Digite outro número inteiro: ')),
     int(input('Digite mais um número inteiro: ')),
     int(input('Digite mais um número inteiro: ')),
     int(input('Digite o último número inteiro: ')))
print(f'Você digitou os valores {n}')
par = int(0)
for c in range(0, len(n)):
    if n[c] % 2 == 0:
        par += 1
print(f'O número 9 apareceu {n.count(9)} vez(es)')
if t3 == 0:
    print('O número 3 não foi digitado em nenhuma posição!')
else:
    print(f'O número 3 foi digitado {n.count(3)} vez(es) e aparece pela primeira vez na posição {n.index(3) + 1}')
print(f'A quantidade de números pares digitados é igual a {par}')
