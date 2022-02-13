from datetime import datetime
dados = {'Nome': str(input('Digite o nome do trabalhador: '))}
nascimento = int(input(f'Digite o ano de nascimento de {dados["Nome"]}: '))
dados['Idade'] = datetime.date.today().year - nascimento
dados['CTPS'] = int(input(f'Digite o número da carteira de trabalho de {dados["Nome"]} (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratacao'] = int(input('Digite o ano de contratação: '))
    dados['Aposentadoria'] = (35 + dados['Contratacao']) - nascimento
    dados['Salário'] = float(input('Qual o salário do funcionário: R$ '))
print('-+=+-' * 6)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
