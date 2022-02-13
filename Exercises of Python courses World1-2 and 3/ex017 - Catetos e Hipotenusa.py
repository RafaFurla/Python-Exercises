#Calcula a hipotenusa de um triângulo retângulo
from math import hypot
ca = float(input('Qual o tamanho do cateto adjacente do triângulo retângulo? '))
co = float(input('Qual o tamanho do cateto oporto do triângulo retângulo? '))
print('O tamanho da hipotenusa do triângulo retãngulo é: {:.2f}'.format(hypot(ca, co)))
