def area(lar, comp):
    a = lar * comp
    print(f'A área do terreno é igual a: {a:.2f} m²!')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-' * 30)
largura = float(input('Qual a largura do terreno em metros? '))
comprimento = float(input('Qual o comprimento do terreno em metros? '))
area(largura, comprimento)
