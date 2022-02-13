info = {"nome": str(input('Digite o nome do jogador: ')).strip()}
info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou? '))
gols = []
for c in range(1, info['partidas'] + 1):
    gols.append(int(input(f'Quantos gols {info["nome"]} fez na {c}ª partida? ')))
info['gols'] = gols[:]
info['Gols no Campeonato'] = sum(gols)  # essa funcionalidade dispensa o contador para fazer o somatório
print('-=' * 43)
print(info)
print('-=' * 43)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 43)
print(f'O jogador {info["nome"]} jogou {info["partidas"]} partidas.')
for p, s in enumerate(info["gols"]):
    print(f'    → Na {p + 1}ª partida {info["nome"]} fez {s} gol(s).')
print(f'Foi um total de {info["Gols no Campeonato"]} gols no campeonato!')
