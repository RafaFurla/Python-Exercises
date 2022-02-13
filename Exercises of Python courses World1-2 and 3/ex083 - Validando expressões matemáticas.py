expressao = str(input('Digite uma expressão matemática: ')).strip()
n = p = k = int(0)  # n conta o número de (, p conta o número de ), k contador
while not k == len(expressao):
    while True:
        if expressao[k] == '(':
            n += 1
        elif expressao[k] == ')':
            p += 1
        if p > n:
            print('Sua expressão é inválida!')
            k = len(expressao)
            break
        k += 1
        if k == len(expressao):
            break
if n > p:
    print('Sua expressão é inválida!')
if n == p:
    print('Sua expressão é válida!')
