# Predefinições
from time import sleep
from random import randint
# Apresentando o software
print('=+=' * 4)
print('JOKENPÔ GAME')
print('=+=' * 4)
# Computador fazendo sua escolha
pc = int(randint(1, 3))
# Jogador fazendo sua escolha
player = int(input('''Choose between:
[1] Rock
[2] Paper
[3] Scissor
'''))
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
# Trocando a variável inteira pela string
if pc == 1:
    pc = str('Rock')
elif pc == 2:
    pc = str('Paper')
elif pc == 3:
    pc = str('Scissor')
if player == 1:
    player = str('Rock')
elif player == 2:
    player = str('Paper')
elif player == 3:
    player = str('Scissor')
# Aplicando as regras do jogo e definindo o vencedor
if pc == player:
    print('Computer choose {}, player choose {}. Tie! Play again!'.format(pc, player))
elif pc == 'Rock' and player == 'Paper':
    print('Computer choose {}, player choose {}. Paper involves Rock! Player wins!'.format(pc, player))
elif pc == 'Rock' and player == 'Scissor':
    print('Computer choose {}, player choose {}. Rock broke scissor! Computer wins!'. format(pc, player))
elif pc == 'Paper' and player == 'Rock':
    print('Computer choose {}, player choose {}. Paper involves Rock! Computer wins!'.format(pc, player))
elif pc == 'Paper' and player == 'Scissor':
    print('Computer choose {}, player choose {}. Scissor cuts the paper! Player wins!'.format(pc, player))
elif pc == 'Scissor' and player == 'Rock':
    print('Computer choose {}, player choose {}. Rock broke scissor! Player wins!'.format(pc, player))
elif pc == 'Scissor' and player == 'Paper':
    print('Computer choose {}, player choose {}. Scissor cuts the paper! Computer wins!'.format(pc, player))
