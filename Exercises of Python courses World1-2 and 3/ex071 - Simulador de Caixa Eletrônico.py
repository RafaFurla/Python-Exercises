print('=' * 40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('=' * 40)
saque = int(input('Informe o valor do saque (valor inteiro): R$ '))
dinheiro = saque
n50 = dinheiro // 50
dinheiro = dinheiro - (n50 * 50)
n20 = dinheiro // 20
dinheiro = dinheiro - (n20 * 20)
n10 = dinheiro // 10
dinheiro = dinheiro - (n10 * 10)
n1 = dinheiro // 1
dinheiro = dinheiro - (n1 * 1)
print(f'Você solicitou R$ {saque:.2f} e receberá: ')
if n50 > 0:
    print(f'{n50} nota(s) de R$ 50,00')
if n20 > 0:
    print(f'{n20} nota(s) de R$ 20,00')
if n10 > 0:
    print(f'{n10} nota(s) de R$ 10,00')
if n1 > 0:
    print(f'{n1} nota(s) de R$ 1,00')
print('-' * 40)
