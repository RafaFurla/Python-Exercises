color = {'clean': '\033[m', 'backwhite': '\033[30;107m', 'backblack': '\033[1;97m',
         'green': '\033[32m', 'blue': '\033[36m'}
print(color['backwhite'], '=+=' * 21, color['clean'])
print(color['backblack'], 'Programa que pega o nome e as notas do aluno e entrega a média!', color['clean'])
print(color['backwhite'], '=+=' * 21, color['clean'])
n = str(input('Qual o nome do aluno? ').strip())
a = float(input('Qual a primeira nota de {}{}{}? '
                .format(color['green'], n, color['clean'])))
b = float(input('Qual a segunda nota de {}{}{}? '
                .format(color['green'], n, color['clean'])))
print('A média final de {}{}{} foi {}{:.1f}{}!'
      .format(color['green'], n, color['clean'],
              color['blue'], (a + b)/2, color['clean']))
