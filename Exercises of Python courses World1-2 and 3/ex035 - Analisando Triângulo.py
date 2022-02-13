# O programa irá ler o comprimento de 3 semiretas e dirá se é possível formar um triângulo com elas.
# Lembrando que a condição é que cada um dos lados seja maior que a soma dos outros 2.
l1 = float(input('Digite o comprimento de 3 segmentos de reta [aperte o enter após cada inserção]: '))
l2 = float(input('                                                                               : '))
l3 = float(input('                                                                               : '))
if l1 < l2+l3:
    if l2 < l1+l3:
        if l3 < l1+l2:
            print('É possível formar um triângulo com esses seguimentos de reta!')
else:
    print('Não é possível formar um triângulo com esses seguimentos de reta!')
