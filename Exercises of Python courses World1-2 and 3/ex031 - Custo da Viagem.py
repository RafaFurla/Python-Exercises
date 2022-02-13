# O programa calculará o preço da passagem sabendo a distância. Para viagens de até 200km o preço por km
# é de R$ 0,50. Para viagens acima de 200km o preço do km rodado é R$ 0,45
k = float(input('Olá! Qual a distância da sua rota em km? '))
preço = k * 0.5 if k <= 200 else k * 0.45
print('O preço da passagem será de: R$ {:.2f}'.format(preço))
