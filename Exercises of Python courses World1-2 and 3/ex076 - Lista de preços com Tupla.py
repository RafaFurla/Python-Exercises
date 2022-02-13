t = (str(input('Digite o nome do produto 1: ')).strip(), float(input('Digite o preço do produto 1: R$ ')),
     str(input('Digite o nome do produto 2: ')).strip(), float(input('Digite o preço do produto 2: R$ ')),
     str(input('Digite o nome do produto 3: ')).strip(), float(input('Digite o preço do produto 3: R$ ')),
     str(input('Digite o nome do produto 4: ')).strip(), float(input('Digite o preço do produto 4: R$ ')),
     str(input('Digite o nome do produto 5: ')).strip(), float(input('Digite o preço do produto 5: R$ ')))
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)
for c in range(0, len(t), 2):
    print(f'{t[c]:.<30}R$ {t[c + 1]:>7.2f}')
print('-' * 40)
