def leiaint(n=""):
    n = str(n)
    while not n.isdecimal():
        n = str(input('Digite um número: ')).strip()
        if not n.isdecimal():
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    n = int(n)
    return n


numero = leiaint()
print(f'Você acabou de digitar o número {numero}')
