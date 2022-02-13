nhvelho = str()
ihvelho = int(0)
soma = float(0)
t = int(0)
for c in range(1, 5):
    nome = str(input('Digite o nome de uma pessoa: '))
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = int(input('Digite o sexo dessa pessoa [1] Masculino / [2] Feminino: '))
    soma = soma + idade
    if sexo == 1 and idade > ihvelho:
        nhvelho = nome
        ihvelho = idade
    if sexo == 2 and idade < 20:
        t = t + 1
print('A média de idade do grupo é de {:.1f} anos!'.format(soma / 4))
print('O homem mais velho da amostra é o {} e ele tem {} anos!'.format(nhvelho, ihvelho))
print('A quantidade de mulheres na amostra que tem menos de 20 anos é de {} mulher(es)!'.format(t))
