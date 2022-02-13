#Lê um número real e mostra somente a parte inteira dele
#Primeiro jeito de fazer
from math import trunc
n = float(input('Digite um número real qualquer: '))
print('A parte inteira do número digitado é: {}'.format(trunc(n)))
#Segundo jeito de fazer
n1 = float(input('Digite um número real qualquer: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(n1, int(n1)))
