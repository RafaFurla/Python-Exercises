color = {'clean': '\033[m', 'blue': '\033[36m', 'purple': '\033[35m', 'green': '\033[32m', 'yellow': '\033[33m'}
print(color['purple'], '=+=' * 23, color['clean'])
print(color['blue'], 'This software calculates the multiplication table of the input number', color['clean'])
print(color['purple'], '=+=' * 23, color['clean'])
n = int(input('Input a integer number that you want to know it´s multiplication table: '))
print('-' * 11)
print(' 0 x {}{}{} = {}{}{}\n 1 x {}{}{} = {}{}{}\n 2 x {}{}{} = {}{}{}\n'
      ' 3 x {}{}{} = {}{}{}\n 4 x {}{}{} = {}{}{}\n 5 x {}{}{} = {}{}{}\n'
      ' 6 x {}{}{} = {}{}{}\n 7 x {}{}{} = {}{}{}\n 8 x {}{}{} = {}{}{}\n'
      ' 9 x {}{}{} = {}{}{}\n10 x {}{}{} = {}{}{}'
      .format(color['green'], n, color['clean'], color['yellow'], n * 0, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 1, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 2, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 3, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 4, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 5, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 6, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 7, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 8, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 9, color['clean'],
              color['green'], n, color['clean'], color['yellow'], n * 10, color['clean']))
print('-' * 11)
