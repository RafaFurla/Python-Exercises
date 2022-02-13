def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isdecimal():
        gols = "0"
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip().capitalize()
g = str(input('Número de gols: ')).strip()
ficha(n, g)
