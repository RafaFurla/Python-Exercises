color = {'green': '\033[32m', 'blue': '\033[36m', 'red': '\033[31m', 'purple': '\033[35m', 'clean': '\033[m'}
print('\033[30;47m=+=\033[m' * 26)
print('\033[30;43mPrograma que descobre o dobro, o triplo e a raíz quadrada do número digitado  \033[m')
print('\033[30;47m=+=\033[m' * 26)
n = int(input('Escreva um número inteiro: '))
print('O dobro de {}{}{} é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{:.3}{}'
      .format(color['green'], n, color['clean'],
              color['blue'], 2 * n, color['clean'],
              color['red'], 3 * n, color['clean'],
              color['purple'], n ** (1/2), color['clean']))
