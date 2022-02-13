s = str(input('Digite o sexo da pessoa. [H] para homem e [M] para mulher: ')).strip().upper()
while (s != 'M') and (s != 'H'):
    s = input('{} não é uma opção válida. Digite [H] para homem e [M] para mulher: '.format(s)).strip().upper()
print('FIM')
if s == 'M':
    print('Sexo feminino registrado com sucesso!')
elif s == 'H':
    print('Sexo masculino registrado com sucesso!')
