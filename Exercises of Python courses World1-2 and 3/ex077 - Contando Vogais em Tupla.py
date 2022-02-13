p1 = str(input('Escreva uma palavra (sem nenhum tipo de acento): ')).strip().upper()
p1 = p1.replace('É', 'E').replace('Ó', 'O').replace('Á', 'A').replace('Í', 'I').replace('Ú', 'U').replace('À', 'A').replace('Ã', 'A').replace('Õ', 'O')
p2 = str(input('Escreva uma palavra (sem nenhum tipo de acento): ')).strip().upper()
p2 = p2.replace('É', 'E').replace('Ó', 'O').replace('Á', 'A').replace('Í', 'I').replace('Ú', 'U').replace('À', 'A').replace('Ã', 'A').replace('Õ', 'O')
p3 = str(input('Escreva uma palavra (sem nenhum tipo de acento): ')).strip().upper()
p3 = p3.replace('É', 'E').replace('Ó', 'O').replace('Á', 'A').replace('Í', 'I').replace('Ú', 'U').replace('À', 'A').replace('Ã', 'A').replace('Õ', 'O')
p = (p1, p2, p3)
for c in range(0, len(p)):
    print('Na palavra {} temos:'.format(p[c]), end=' ')
    for k in range(0, len(p[c])):
        if p[c][k] in 'AEIOU':
            print(p[c][k], end=' ')
    print('')
