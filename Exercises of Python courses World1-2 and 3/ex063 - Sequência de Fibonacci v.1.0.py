p = int(input('Quantos termos da sequência de Fibonacci você quer ver? '))
a1 = int(0)
a2 = int(1)
if p == 0:
    print('Não há termos digitados!')
elif p == 1:
    print(a1)
elif p == 2:
    print(a1, ' → ', a2)
elif p != 0 and 1 and 2:
    print(a1, ' → ', a2, ' → ', end=' ')
    p = p - 2
    while p > 1:
        a1 = a1 + a2
        a2 = a2 + a1
        print(a1, ' → ', a2, ' → ', end=' ')
        p = p - 1
print('Fim!')
