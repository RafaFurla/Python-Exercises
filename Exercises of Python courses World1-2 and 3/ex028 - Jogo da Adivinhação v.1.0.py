#O usuário via tentar adivinhar qual número entre 0 e 5 o computador escolheu.
from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 23)
p = int(input('Tente adivinhar qual número entre 0 e 5 o computador escolheu: '))
print('-=-' * 23)
print('Processando...')
sleep(2)
if n == p:
    print('Parabéns você acertou! O número que o computador escolheu realmente é o {}!!!'.format(n))
else:
    print('Infelizmente você errou! O número que o computador escolheu era o {}. Tente mais vezes!'.format(n))
