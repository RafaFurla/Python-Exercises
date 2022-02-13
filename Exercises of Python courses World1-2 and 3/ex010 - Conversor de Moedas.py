color = {'clean': '\033[m', 'backgray': '\033[1;30;107m', 'green': '\033[32m'}
print(color['backgray'], '[+]' * 16, color['clean'])
print(color['backgray'], ' This software converts the real coin to dollar ', color['clean'])
print(color['backgray'], '[+]' * 16, color['clean'])
r = float(input('How many reais do you have in your pocket? '))
d = r / 3.27  # Now we are converting the R$ in US$ admitting that the tax of conversion is 3.27
print('With R$ {}{:.2f}{} you can buy US$ {}{:.2f}{}'
      .format(color['green'], r, color['clean'], color['backgray'], d, color['clean']))
