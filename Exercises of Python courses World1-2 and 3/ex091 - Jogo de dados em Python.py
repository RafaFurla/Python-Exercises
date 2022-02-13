from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado!')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# itemgetter(0) corresponde às chaves (keys = jogador1, jogador2, ...)
# itemgetter(1) corresponde aos valores (values = números sorteados randomicamente).
# Portanto o itemgetter consegue acessar os itens dos dicionários como se fossem uma lista com os indexadores numéricos.
# O Itemgeter transforma o dicionário em uma lista, portanto o ranking a partir de agora deve ser tratado como uma lista.
print('-+-' * 20)
print(f'{"Ranking dos jogadores":^33}')
for k, v in enumerate(ranking):
    print(f'    {k+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
