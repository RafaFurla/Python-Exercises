#Sorteando a ordem de apresentação do trabalho (usando o método shuffle)
import random
n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('Qual o nome do segundo aluno? '))
n3 = str(input('Qual o nome do terceiro aluno? '))
n4 = str(input('Qual o nome do quarto aluno? '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
#O shuffle troca a ordem da lista lá na memória, portanto não precisa da criação de uma nova variável
print(lista)
#Outro método usando o sample
embaralhar = random.sample(lista, k=4)
#k significa a quantidade de membros do grupo que serão incluídos
print('A ordem de apresentação é {}'.format(embaralhar))
