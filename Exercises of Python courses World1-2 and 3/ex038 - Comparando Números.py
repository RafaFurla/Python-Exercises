color = {'clean': '\033[m', 'backblue': '\033[0;31;44m'}
print(color['backblue'], '-+-' * 21, color['clean'])
print(color['backblue'], 'This software analyzes two numbers to say which is the biggest ', color['clean'])
print(color['backblue'], '-+-' * 21, color['clean'])
n1 = int(input('Input a integer number: '))
n2 = int(input('Input other integer number: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe valor maior, os dois números são iguais!')
