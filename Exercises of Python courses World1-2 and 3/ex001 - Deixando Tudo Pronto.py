# Para fazer comentários dentro do python é só iniciar a linha com o símbolo de hashtag #
cores = {'verde': '\033[32m', 'limpa': '\033[m', 'azul': '\033[36m'}
msg = str('Hello World!')
print(msg)
print('=+=' * 14)
print('REVELANDO O TIPO PRIMITIVO DAS VARIÁVEIS')
print('=+=' * 14)
n1 = int((input('Digite um número: ')))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'
      .format(cores['verde'], n1, cores['limpa'],
              cores['verde'], n2, cores['limpa'],
              cores['azul'], s, cores['limpa']))
print('O tipo primitivo da variável n1 é: \033[36m{}\033[m'.format(type(n1)))
print('O tipo primitivo da variável n2 é: \033[36m{}\033[m'.format(type(n2)))
print('O tipo primitivo da variável s é: \033[36m{}\033[m'.format(type(s)))
