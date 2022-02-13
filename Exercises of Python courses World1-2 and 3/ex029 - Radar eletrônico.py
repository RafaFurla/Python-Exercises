# O programa vai ler a velocidade do carro e se passar de 80km/h vai aplicar uma multa que custará
# 7,00 para cada km/h acima de 80km/h
v = float(input('Qual a sua velocidade em km/h? '))
if v>80:
    print('Você ultrapassou a velocidade permitida que era de 80km/h! Você foi multado! A multa lhe custará: R$ {:.2f}'.format(7*(v-80)))
else:
    print('Tenha um bom dia! Dirija com segurança!')