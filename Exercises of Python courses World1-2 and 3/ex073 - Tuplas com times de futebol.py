cla = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
       'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
       'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {cla[0: 5]}')
print(f'Os últimos 4 colocados são: {cla[-4:]}')
print(f'Os times participantes da série A, em ordem alfabética são: {sorted(cla)}')
print(f'O time da Chapecoense está na {cla.index("Chapecoense") + 1}ª posição da série A do brasileirão!')
