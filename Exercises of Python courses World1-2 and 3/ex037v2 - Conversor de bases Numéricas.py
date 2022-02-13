num = int(input('Digite um número inteiro: '))
opção = int(input('''Digite uma das opções a seguir: 
[1] Binário
[2] Octal
[3] Hexadecimal
Escolha um dos números acima que representa a base que você quer a conversão: '''))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Somente as opções 1, 2 ou 3 são válidas! A opção {} não é válida! Tente novamente!'.format(opção))
