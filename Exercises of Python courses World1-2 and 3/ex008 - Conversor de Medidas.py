color = {'clean': '\033[m', 'red': '\033[31m', 'green': '\033[32m'}
print(color['red'], '=+=' * 21, color['clean'])
print(' The script convert one measure in meters to other magnitudes')
print(color['red'], '=+=' * 21, color['clean'])
n = float(input('Input a measure in meters: '))
print('{}{}{} meter(s) is equal to:\n{}{}{} kilometer(s)\n{}{}{} hectometer(s)'
      '\n{}{}{} dekameter(s)\n{}{}{} decimeter(s)\n{}{}{} centimeter(s)'
      '\n{}{}{} millimeter(s)'
      .format(color['green'], n, color['clean'],
              color['red'], n/1000, color['clean'],
              color['red'], n/100, color['clean'],
              color['red'], n/10, color['clean'],
              color['red'], n*10, color['clean'],
              color['red'], n*100, color['clean'],
              color['red'], n*1000, color['clean']))
