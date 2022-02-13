def escreva(texto):
    print('~' * (len(texto)+6))
    print(f'{texto.center(len(texto) + 6, " ")}')
    print('~' * (len(texto)+6))


mensagem = str(input('Digite a mensagem que você quer que apareça formatada: ')).strip().upper()
escreva(mensagem)
