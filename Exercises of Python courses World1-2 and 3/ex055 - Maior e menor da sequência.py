ma = float(0)
me = float(0)
for c in range(1, 6):
    peso = float(input('Digite o peso (em kg) do {}º candidato: '.format(c)))
    if c == 1:
        ma = peso
        me = peso
    else:
        if peso >= ma:
            ma = peso
        if peso <= me:
            me = peso
print('O maior peso digitado foi {} kg e o menor {} kg!'.format(ma, me))
