a1 = int(input('Input the first term of a A.P.: '))
r = int(input('Input the period of the A.P.: '))
q = int(1)
while q < 11:
    print(a1 + (q - 1) * r, '→', end=' ')
    q += 1
print('Esses são os 10 primeiros termos!')
resp = int(1)
while resp != 0:
    resp = int(input('Quer mostrar mais quantos termos? '))
    if resp != 0:
        for resp in range(0, resp, 1):
            print(a1 + (q + resp - 1) * r, '→', end=' ')
    else:
        print('Fim')
