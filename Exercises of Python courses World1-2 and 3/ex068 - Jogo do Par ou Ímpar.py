from random import randint
cont = int(0)
print('=+=' * 9)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=+=' * 9)
while True:
    c = int(randint(0, 10))
    j = int(input('Diga um valor: '))
    e = str(' ')
    while e not in 'PpIi':
        e = str(input('Você escolhe Par ou Ímpar? [P/I] ')).strip().upper()[0]
    k = (j + c) % 2
    if e == 'P':
        if k == 0:
            print(f'Você jogou {j} e o computador {c}. Total de {j+c}! Deu PAR! ')
            print('Você venceu! Parabéns!')
            cont += 1
        elif k == 1:
            print(f'Você jogou {j} e o computador {c}. Total de {j + c}! Deu ÍMPAR! ')
            print('Você perdeu!')
            break
    if e == 'I':
        if k == 0:
            print(f'Você jogou {j} e o computador {c}. Total de {j+c}! Deu PAR! ')
            print('Você perdeu!')
            break
        elif k == 1:
            print(f'Você jogou {j} e o computador {c}. Total de {j + c}! Deu ÍMPAR! ')
            print('Você venceu! Parabéns!')
            cont += 1
print(f'Game over! Você venceu {cont} vez(es)!')
