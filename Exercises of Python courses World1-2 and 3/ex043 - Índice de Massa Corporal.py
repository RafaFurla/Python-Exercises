print('This software calculates the IMC of a person with the given height and weight!')
a = float(input('Input your height in m: '))
p = float(input('Input your weight in kg: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Abaixo do peso! IMC = {}'.format(imc))
if 18.5 < imc < 25:
    print('Peso ideal! IMC = {}'.format(imc))
if 25 < imc < 30:
    print('Sobrepeso! IMC = {}'.format(imc))
if 30 < imc < 40:
    print('Obesidade! IMC = {}'.format(imc))
if imc > 40:
    print('Obesidade mórbida! IMC = {}'.format(imc))
