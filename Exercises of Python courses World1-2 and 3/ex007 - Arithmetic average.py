color = {'clean': '\033[m', 'backwhite': '\033[30;107m', 'backblack': '\033[1;97m',
         'green': '\033[32m', 'blue': '\033[36m'}
print(color['backwhite'], '=+=' * 21, color['clean'])
print(color['backblack'], 'Script that gets the grades of the students and output the average grade!', color['clean'])
print(color['backwhite'], '=+=' * 21, color['clean'])
n = str(input('Who is the first student? ').strip())
a = float(input('What is the first grade of {}{}{}? '
                .format(color['green'], n, color['clean'])))
b = float(input('What is the second grade of {}{}{}? '
                .format(color['green'], n, color['clean'])))
print('The final average of {}{}{} is {}{:.1f}{}!'
      .format(color['green'], n, color['clean'],
              color['blue'], (a + b)/2, color['clean']))
