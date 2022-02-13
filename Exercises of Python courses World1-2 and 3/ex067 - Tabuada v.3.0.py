while True:
    n = int(input('Quer ver a tabuada de qual valor? (número negativo finaliza programa): '))
    print(70 * '_')
    if n < 0:
        break
    for p in range(0, 11):
        print(f'{p:2} x {n} = {p * n}')
    print(70 * '_')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
