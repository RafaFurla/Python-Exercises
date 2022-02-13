#Aluguel de carros. Obs.: o carro custa R$ 60,00/dia e R$ 0,15 por km rodado
d = int(input('Por quantos dias você ficou com o carro? '))
k = float(input('Dirigiu quantos km com o carro? '))
print('O preço final do aluguel do carro é R$ {:.2f}'.format((d * 60)+(k * 0.15)))
