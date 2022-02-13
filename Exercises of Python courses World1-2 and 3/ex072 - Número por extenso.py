print('=+=' * 20)
print('{:^60}'.format('NÚMERO POR EXTENSO'))
print('=+=' * 20)
n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorse', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(-1)
r = 'S'
while r == 'S':
    while num < 0 or num > 20:
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'O número que você digitou é o {n[num]}')
    while True:
        r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
    num = (-1)
