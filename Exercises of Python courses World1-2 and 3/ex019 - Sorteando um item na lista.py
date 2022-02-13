#Sorteando um dos 4 alunos para apagar o quadro
from random import choice
n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('Qual o nome do segundo aluno? '))
n3 = str(input('Qual o nome do terceiro aluno? '))
n4 = str(input('Qual o nome do quarto aluno? '))
list = [n1, n2, n3, n4]
sorteio = choice(list)
print('O aluno escolhido para apagar o quadro foi {}'.format(sorteio))
