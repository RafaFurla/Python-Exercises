#Cálculo seno, cosseno e tangente de um dado ângulo. Obs.: para as funções trigonométricas o ângulo deve
#estar em radianos
import math
a = float(input('Digite um ângulo: '))
print('O seno de {:.2f}º é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(a, math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
