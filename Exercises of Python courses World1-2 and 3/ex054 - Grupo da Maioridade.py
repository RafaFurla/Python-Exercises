from datetime import date
ma = int(0)
me = int(0)
for c in range(1, 8):
    nome = str(input('Digite o nome de uma pessoa: '))
    nasc = int(input('Digite o ano de nascimento de {}: '.format(nome)))
    dif = date.today().year - nasc
    if dif >= 21:  # consideramos que atingiram a maioridade as pessoas que tem 21 anos ou mais
        ma = ma + 1
    else:
        me = me + 1
print('Dentro dessa amostra temos {} pessoas que atingiram a maioridade e {} ainda não!'.format(ma, me))
