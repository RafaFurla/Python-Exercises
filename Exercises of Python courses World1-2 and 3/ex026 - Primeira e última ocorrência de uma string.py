f = str(input('Escreva uma frase: ')).strip().upper()
print('A letra "A" aparece {} vez(es) na frase digitada!'.format(f.count('A')))
print('A letra "A" aparece a primeira vez na {}ª posição dentro da frase!'.format(f.find('A')+1))
print('A letra "A" aparece a última vez na {}ª posição dentro da frase!'.format(f.rfind('A')+1))
