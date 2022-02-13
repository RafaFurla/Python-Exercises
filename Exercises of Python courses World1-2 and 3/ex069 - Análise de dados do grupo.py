contM = contI = contF20 = int(0)
r = str('P')
while True:
    print('CADASTRE UMA PESSOA')
    while True:
        s = str(input('Qual o sexo pessoa? ([M] para masculino, [F] para feminino) ')).strip().upper()[0]
        if s == 'M' or s == 'F':
            break
    i = int(input('Qual a idade da pessoa? '))
    if i > 18:
        contI += 1
    if s == 'M':
        contM += 1
    if s == 'F' and i < 20:
        contF20 += 1
    while True:
        r = str(input('Quer continuar [S/N]? ')).strip().upper()
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break
print(f'''Quantidade de pessoas com mais de 18 anos: {contI}
Quantidade de homens cadastrados: {contM}
Quantidade de mulheres com menos de 20 anos: {contF20}''')
