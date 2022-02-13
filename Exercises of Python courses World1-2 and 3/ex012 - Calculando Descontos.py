# Calcula o desconto de um produto. Obs.: o desconto é de 5%.
p = float(input('Coloque o preço normal do produto para que possamos calcular o desconto: '))
print('O valor do desconto é de {:.2f} reais e o novo preço do produto é de {:.2f} reais!'.format(p * 0.05, p - (p * 0.05)))
