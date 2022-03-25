colors = {'clean': '\033[m', 'green': '\033[32m', 'yellow': '\033[33m', 'red': '\033[31m'}
print('\033[35m-#-\033[m' * 20)
print('\033[36mScript that print the predecessor and the successor of the input number\033[m')
print('\033[35m-#-\033[m' * 20)
n = int(input('Input a integer number: '))
print('''The predecessor number of the number {}{}{} is the number {}{}{} and the successor is the 
number {}{}{}'''.format(colors['green'], n, colors['clean'],
                            colors['yellow'], n - 1, colors['clean'],
                            colors['red'], n + 1, colors['clean']))
