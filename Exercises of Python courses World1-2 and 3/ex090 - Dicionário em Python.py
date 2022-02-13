print('-+-' * 20)
print('{:^60}'.format('NOME, MÉDIA E SITUAÇÃO DO ALUNO'))
print('-+-' * 20)
nms = {'nome': str(input('Diga seu nome: '))}
while True:
    nms['media'] = float(input(f'Diga a média de {nms["nome"]}: '))
    if 0 <= nms['media'] <= 10:
        break
    else:
        print('A média tem que estar entre os valores de 0 a 10.')
if 7 <= nms['media'] <= 10:
    nms['situacao'] = 'Aprovado'
elif 5 <= nms['media'] < 7:
    nms['situacao'] = 'Recuperação'
elif 0 <= nms['media'] < 5:
    nms['situacao'] = 'Reprovado'
for k, v in nms.items():
    print(f'    → {k} é igual a {v}')
