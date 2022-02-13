print('-' * 50)
print(f'{"SOFTWARE PARA AVALIAÇÃO DE JOGADORES":^50}')
print('-' * 50)
r = str('Y')
gols = []
totalgols = int(0)
new = []
while True:
    r = str('Y')
    totalgols = int(0)
    info = {"nome": str(input('Digite o nome do jogador: ')).strip()}
    info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou? '))
    for c in range(1, info['partidas'] + 1):
        gols.append(int(input(f'Quantos gols {info["nome"]} fez na {c}ª partida? ')))
        totalgols += gols[c - 1]
    info['gols'] = gols[:]
    info['Gols no Campeonato'] = totalgols
    new.append(info.copy())
    info.clear()
    gols.clear()
    while r != 'S' and r != 'N':
        r = str(input('Você quer continuar? ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 43)
print(f'{"cod":3} {"nome":12} {"gols":20}{"total":5}')
print('-' * 52)
for c in range(0, len(new)):
    print(f'{c:<4}{new[c]["nome"]:<13}', end='')
    print(f'{new[c]["gols"]}', end='')
    print(' ' * (20 - (3 * new[c]["gols"].__len__())), end='')  # Outra maneira de fazer esse margeamento é  {v["Gols"]!s:<15s}. Esse !s:s converte uma lista em str temporariamente.
    print(new[c]["Gols no Campeonato"])
print('-' * 52)
resposta = int(0)
print(len(new))
while True:
    while True:
        resposta = int(input('Mostrar dados de qual jogador? [Escolher um dos "Cod" na tabela acima][999 para encerrar] '))
        if resposta == 999:
            break
        elif resposta < 0 or resposta >= len(new):
            print(f'Erro! Não existe jogardor com o código {resposta}! Tente novamente!')
        elif 0 <= resposta < len(new):
            break
    if resposta == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {new[resposta]["nome"]}')
    for c in range(0, new[resposta]["gols"].__len__()):
        print(f'    No jogo {c + 1} fez {new[resposta]["gols"][c]} gol(s)')
print('<< VOLTE SEMPRE >>')
