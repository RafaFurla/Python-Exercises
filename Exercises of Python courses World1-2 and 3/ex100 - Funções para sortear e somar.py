from random import randint
from time import sleep
numeros = []


def sorteia(listas):
    """
    sorteia é uma função que cria valores inteiros aleatórios (entre zero e vinte) para fazer parte de uma lista.
    :param listas:
    :return:
    """
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(0, 5):
        listas.append(randint(0, 20))
        sleep(0.3)
        print(listas[c], end=' ')
    print('- PRONTO!')


def somapar(listas):
    somap = int(0)
    for c in listas:
        if c % 2 == 0:
            somap += c
    print(f'A soma de todos os números pares dentro da lista: {listas} é: {somap}')


sorteia(numeros)
somapar(numeros)
