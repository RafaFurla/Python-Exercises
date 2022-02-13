from time import sleep
from random import randint
color = {'clean': '\33[m', 'red': '\33[1;31m'}
print(color['red'], '=+=' * 20, color['clean'])
print('{}GUESSING GAME{}'.format(' ' * 23, ' ' * 23))
print(color['red'], '=+=' * 20, color['clean'])
print('        Computer is choosing a number between 1 and 10!')
print(' Wait', end='')
for c in range(1, 8):
    sleep(0.3)
    print('.', end='')
pc = int(randint(1, 10))
print('')
print(' Computer chooses his number!')
t = int(0)
correct = bool(False)
while not correct:
    player = int(input(' Try to guess: '))
    t += 1
    if player == pc:
        correct = True
print(' You got it! The number the computer chose is actually {}! You succeeded in {} attempt(s)! Congratulations!'.format(player, t))
