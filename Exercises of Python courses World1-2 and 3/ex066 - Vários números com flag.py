s = p = int(0)
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    s += n
    p += 1
print(f'A soma dos {p} números digitados é igual a {s}')
