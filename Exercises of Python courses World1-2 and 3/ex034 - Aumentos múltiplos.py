# Pergunta o salário de um funcionário e calcula seu aumento. Para salários maiores que R$ 1.250,00
# aumento de 10% para menores aumento de 15%.
s = float(input('Digite seu salário: R$ '))
if s >= 1250:
    print('O aumento em seu salário será de 10% (R$ {:.2f})! '
          'Portando seu novo salário passará a R$ {:.2f}'.format(s*0.1, s+(s * 0.1)))
else:
    print('O aumento em seu salário será de 15% (R$ {:.2f})! '
          'Portando seu novo salário passará a R$ {:.2f}'.format(s * 0.15, s + (s * 0.15)))
