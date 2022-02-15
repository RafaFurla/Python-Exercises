# input '#' to make coments inside python!
colors = {'green': '\033[32m', 'clean': '\033[m', 'blue': '\033[36m'}
msg = str('Hello World!')
print(msg)
print('=+=' * 14)
print('REVEALING THE CLASS OF THE OBJECTS')
print('=+=' * 14)
n1 = int((input('Input a integer number: ')))
n2 = int(input('Input other integer number: '))
s = n1 + n2
print('The sum between {}{}{} and {}{}{} is equal to {}{}{}'
      .format(colors['green'], n1, colors['clean'],
              colors['green'], n2, colors['clean'],
              colors['blue'], s, colors['clean']))
print('The class of the object n1 is: \033[36m{}\033[m'.format(type(n1)))
print('The class of the object n2 is: \033[36m{}\033[m'.format(type(n2)))
print('The class of the object s is: \033[36m{}\033[m'.format(type(s)))
