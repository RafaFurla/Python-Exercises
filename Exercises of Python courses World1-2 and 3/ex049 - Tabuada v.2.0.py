n = int(input('Choose a number to know his multiplication table: '))
for c in range(0, 11, 1):
    print('{} x {:2} = {}'.format(n, c, n * c))
