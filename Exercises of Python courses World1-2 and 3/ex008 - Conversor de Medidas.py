color = {'clean': '\033[m', 'red': '\033[31m', 'green': '\033[32m'}
print(color['red'], '=+=' * 21, color['clean'])
print(' O programa converte uma medida em metros para as outras escalas')
print(color['red'], '=+=' * 21, color['clean'])
n = float(input('Escreva uma medida em metros: '))
print('{}{}{} metro(s) é igual a:\n{}{}{} quilômetro(s)\n{}{}{} hectômetro(s)'
      '\n{}{}{} decâmetro(s)\n{}{}{} decimetro(s)\n{}{}{} centímetro(s)'
      '\n{}{}{} milímetro(s)'
      .format(color['green'], n, color['clean'],
              color['red'], n/1000, color['clean'],
              color['red'], n/100, color['clean'],
              color['red'], n/10, color['clean'],
              color['red'], n*10, color['clean'],
              color['red'], n*100, color['clean'],
              color['red'], n*1000, color['clean']))
