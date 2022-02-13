vetor = list()
r = str('Y')
while r != 'N':
    nome = str(input('Digite o nome do aluno: ')).strip()
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input('Digite a 2ª nota do aluno: '))
    media = (nota1 + nota2) / 2
    vetor.append([nome, [nota1, nota2], media])
    r = str('Y')
    while r != 'S' and r != 'N':
        r = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
print('=+' * 14)
print('Nº   NOME              MÉDIA')
print('-' * 28)
for c, k in enumerate(vetor):
    print(f'{c:<3}  ', end='')
    print(f'{k[0]:<18} ', end='')
    print(f'{k[2]}')
print('-' * 28)
opcao = int(0)
while opcao != 999:
    opcao = int(input('Quer mostrar as notas de qual aluno[Nº]? (999 para interromper): '))
    if 0 <= opcao < len(vetor):
        print(f'As notas de {vetor[opcao][0]} são: {vetor[opcao][1]}')
    elif opcao == 999:
        print('FINALIZANDO...')
    else:
        print('Você não digitou uma opção válida: ')
print('<<<VOLTE SEMPRE>>>')
