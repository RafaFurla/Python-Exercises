matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Se eu não colocar valores genéricos agora a matriz não aceitará receber os elementos diretamente na hora da repetição
par = sc3 = ma = int(0)
for i in range(0, 3):
    for j in range(0, 3):
        matr[i][j] = int(input(f'Digite um valor inteiro para a posição: [{i}, {j}]: '))
        if matr[i][j] % 2 == 0:
            par += matr[i][j]
        if j == 2:
            sc3 += matr[i][j]
        if i == 1 and j == 0:
            ma = matr[i][j]
        if i == 1 and j > 0:
            if matr[i][j] > ma:
                ma = matr[i][j]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matr[i][j]:^5}]', end='')
    print()
print(f'A soma dos valores pares digitados é {par}')
print(f'A soma dos valores da 3a coluna é: {sc3}')
print(f'O maior valor da 2a linha é {ma}')
