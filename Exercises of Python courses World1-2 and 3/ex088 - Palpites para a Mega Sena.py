# Definindo os parâmetros, apresentação e imputs:
from random import randint
from time import sleep
from math import factorial
jogo = []
game = list()
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
espacos = int(16)
while espacos < 6 or espacos > 15:
    espacos = int(input('Quantos números você quer marcar por jogo? '))
    if espacos < 6 or espacos > 15:
        print('Pelas regras do jogo você deve marcar entre 6 e 15 números!')
combinacao = float(((factorial(60)) / ((factorial(6)) * (factorial(60 - 6)))) /
                   ((factorial(espacos)) / ((factorial(6)) * (factorial(espacos - 6)))))
vezes = combinacao + 1
while vezes > combinacao:
    vezes = int(input(f'Quantos jogos você quer que eu sorteie? (Limite: {combinacao:.0f}): '))
    if vezes > combinacao:
        print(f'A quantidade de jogos solicitados é maior que a quantidade máxima de combinações que é: {combinacao:.0f}')
print('-=' * 4, end=' ')
print(f'SORTEANDO {vezes} JOGOS', end=' ')
print('-=' * 4)
# iniciando cálculos
for c in range(0, vezes):
    while True:
        for p in range(0, espacos):
            while True:
                num = randint(1, 60)
                if num not in jogo:
                    jogo.append(num)
                    break
        jogo.sort()
        if jogo not in game:
            game.append(jogo[:])
            jogo.clear()
            break
        jogo.clear()
    print(f'Jogo {c + 1}: {game[c]}')
# Apresentando os Resultados
sleep(0.5)
print('-=' * 5, end=' ')
print(f'< BOA SORTE >', end=' ')
print('-=' * 5)
