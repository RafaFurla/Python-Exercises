cores = {'limpa': '\033[m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'vermelho': '\033[31m'}
print('\033[35m-#-\033[m' * 20)
print('\033[36mPrograma que diz o número anterior e o posterior ao digitado!\033[m')
print('\033[35m-#-\033[m' * 20)
n = int(input('Escreva um número inteiro: '))
print('''O número anterior ao número {}{}{} é o número {}{}{} e o posterior 
é o número {}{}{}'''.format(cores['verde'], n, cores['limpa'],
                            cores['amarelo'], n-1, cores['limpa'],
                            cores['vermelho'], n+1, cores['limpa']))
