# Calcula a área de uma parede e diz quantos litros de tinta são necessários para pintá-la.
# Obs.: 1 litro de tinta pinta 2m**2.
h = float(input('Qual a altura da parede em metros? '))
o = float(input('Qual a largura da parede em metros? '))
print('A quantidade de tinta necessária para pintar a parede é(são) {:.2f} litro(s) de tinta'.format((h * o)/2))
