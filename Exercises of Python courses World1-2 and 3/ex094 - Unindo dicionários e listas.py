r = sexo = str('Y')
idadetotal = int(0)
dados = {}
listatotal = []
listamulheres = []
listaacimamedia = []
while True:
    r = sexo = str('Y')
    dados['nome'] = str(input('Digite o nome: ')).strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Digite a idade: '))
    listatotal.append(dados.copy())
    idadetotal += dados['idade']
    if sexo == 'F':
        listamulheres.append(dados.copy())
    dados.clear()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
idademedia = idadetotal / len(listatotal)
print()
print('-+-' * 25)
print(f'{"RESULTADOS":^75}')
print()
print(f'- O grupo tem {len(listatotal)} pessoas.')
print(f'- A média de idade é de {idademedia:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end=" ")
for k, v in enumerate(listamulheres):
    print(listamulheres[k]['nome'], end=' ')
print('')
print(f'- Lista de pessoas com idade acima da média:')
for k, v in enumerate(listatotal):
    if listatotal[k]['idade'] > idademedia:
        listaacimamedia.append(listatotal[k])
for k in range(0, len(listaacimamedia)):
    print(f'nome = {listaacimamedia[k]["nome"]}; sexo = {listaacimamedia[k]["sexo"]}; idade = {listaacimamedia[k]["idade"]}')
print('<< ENCERRADO >>')
