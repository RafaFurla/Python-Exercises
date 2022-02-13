from utilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p, False)}')
print(f'O dobro de {p} é {moeda.dobro(p, False)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, False)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13, False)}')
