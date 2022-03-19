import uteis108
p = float(input('Digite o preço: R$ '))
print(f'A metade de {uteis108.moeda(p)} é {uteis108.moeda(uteis108.metade(p))}')
print(f'O dobro de {uteis108.moeda(p)} é {uteis108.moeda(uteis108.dobro(p))}')
print(f'Aumentando 10% temos {uteis108.moeda(uteis108.aumentar(p, 10))}')
print(f'Reduzindo 13% temos {uteis108.moeda(uteis108.diminuir(p, 13))}')
