parimpar = [[], []]
for c in range(0, 7):
    if c == 0:
        num = int(input('Digite um número inteiro: '))
    else:
        num = int(input('Digite outro valor: '))
    if num % 2 == 0:
        parimpar[0].append(num)
    else:
        parimpar[1].append(num)
parimpar[0].sort()
parimpar[1].sort()
print(f'Os números pares digitados em ordem crescente são: {parimpar[0]}\nOs números ímpares digitados em ordem crescente são: {parimpar[1]}')
