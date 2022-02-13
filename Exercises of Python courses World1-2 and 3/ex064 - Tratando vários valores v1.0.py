color = {'clean': '\033[m', 'green': '\033[32m'}
n = int(input('Input a integer number [input 999 to stop the program]: '))
s = int(0)
while n != 999:
    s += n
    n = int(input('Input other number [input 999 to stop the program]: '))
print('{}The sum of the input numbers are: {}{}'.format(color['green'], s, color['clean']))
