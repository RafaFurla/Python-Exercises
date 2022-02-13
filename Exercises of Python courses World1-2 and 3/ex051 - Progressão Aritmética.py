a1 = int(input('Input the first term of the A.P.: '))
r = int(input('Input the period of the arithmetic progression: '))
a10 = a1 + (10 - 1) * r
s = int(0)
for c in range(a1, a10 + r, r):
    s = s + c
    print('{} → '.format(c), end='')  # pra colocar essa setinha devo apertar alt+26
print('It´s over!')
print('The sum of the first 10 terms of this A.P. is equal to: {}'.format(s))

