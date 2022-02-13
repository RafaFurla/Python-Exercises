num = list()
for c in range(0, 5):
    n = int(input('Digite um número inteiro: '))
    if c == 0:
        num.append(int(n))
        print('Adicionado na posição 0 da lista...')
    else:
        if n > max(num):
            num.append(int(n))
            print('Adicionado na posição final da lista...')
        elif n < min(num):
            num.insert(0, n)
            print('Adicionado na posição 0 da lista...')
        else:
            for k in range(len(num) - 1, 0, -1):
                cont = False
                while not cont:
                    if num[k - 1] <= n < num[k]:
                        num.insert(k, n)
                        print(f'Adicionado na posição {k} da lista...')
                        cont = True
                    cont = True
print(num)
