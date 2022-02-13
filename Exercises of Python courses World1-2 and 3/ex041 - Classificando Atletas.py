color = {'clean': '\033[m', 'blue': '\033[1;34m', 'backyellow': '\033[30;43m', 'backgreen': '\033[1;97;42m'}
print(color['backyellow'], '=+=' * 38, color['clean'])
print(color['backgreen'], ' This software is design for the National Swimming Confederation for categorize athletes'
      ' according with their age!', color['clean'])
print(color['backyellow'], '=+=' * 38, color['clean'])
age = int(input('What is the athlete´s age? '))
if age <= 9:
    print('{}MIRIM{}'.format(color['blue'], color['clean']))
elif 9 < age <= 14:
    print('{}INFANTIL{}'.format(color['blue'], color['clean']))
elif 14 < age <= 19:
    print('{}JUNIOR{}'.format(color['blue'], color['clean']))
elif 19 < age <= 20:
    print('{}SÊNIOR{}'.format(color['blue'], color['clean']))
elif age > 20:
    print('{}MASTER{}'.format(color['blue'], color['clean']))
