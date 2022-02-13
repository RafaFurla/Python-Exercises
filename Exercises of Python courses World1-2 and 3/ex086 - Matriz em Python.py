matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Se eu não colocar valores genéricos agora a matriz não aceitará receber os elementos diretamente na hora da repetição
for i in range(0, 3):
    for j in range(0, 3):
        matr[i][j] = int(input(f'Digite um valor para a posição: [{i}, {j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matr[i][j]:^5}]', end='')
    print()