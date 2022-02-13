palavra = str(input('Digite alguma coisa: '))
print('O tipo primitivo desse valor é {}'.format(palavra.__class__))
print('O tipo primitivo desse valor é: ', type(palavra))  # outro jeito de fazer a mesma coisa
print('Só tem espaços? {}'.format(palavra.isspace()))
print('É um número? {}'.format(palavra.isnumeric()))  # aceita caracteres do tipo: ½, ¼, ¹, ², ³
print('É decimal? {}'.format(palavra.isdecimal()))  # só aceita números no teclado padrão: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
print('É somente formado por dígitos? {}'.format(palavra.isdigit()))  # aceita caracteres do tipo: ¹, ², ³
print('É alfabético? {}'.format(palavra.isalpha()))
print('É alfanumérico? {}'.format(palavra.isalnum()))
print('Está em maiúsculas? {}'.format(palavra.isupper()))
print('Está em minúsculas? {}'.format(palavra.islower()))
print('Está capitalizada? {}'.format(palavra.istitle()))
