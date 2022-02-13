a1 = int(input('Input the first term of a A.P.: '))
r = int(input('Input the period of the A.P.: '))
q = int(1)
while q < 11:
    print(a1 + (q - 1) * r, '→', end=' ')
    q += 1
print('Fim')
