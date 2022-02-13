from time import sleep


def contador(inicio, fim, passo):
    print("=" * 50)
    if passo == 0:
        if inicio > fim:
            passo = -1
        elif inicio < fim:
            passo = 1
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if inicio <= fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
            sleep(0.1)
    if inicio > fim:
        for c in range(inicio, fim - 1, passo):
            print(c, end=" ")
            sleep(0.1)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, -2)
print("=" * 50)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
