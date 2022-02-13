nomepeso = []
maipes = list()
menpes = []
r = str('Y')
totpes = int(0)
while r != 'N':
    nomepeso.append(str(input('Digite o nome: ')).strip())
    nomepeso.append(float(input('Digite o peso (kg): ')))
    totpes += 1
    if totpes == 1:
        maipes.append(nomepeso[:])
        menpes.append(nomepeso[:])
    else:
        if nomepeso[1] > maipes[0][1]:
            maipes.clear()
            maipes.append(nomepeso[:])
        elif nomepeso[1] == maipes[0][1]:
            maipes.append(nomepeso[:])
        if nomepeso[1] < menpes[0][1]:
            menpes.clear()
            menpes.append(nomepeso[:])
        elif nomepeso[1] == menpes[0][1]:
            menpes.append(nomepeso[:])
    nomepeso.clear()
    while True:
        r = str(input('Você quer continuar? ')).strip().upper()[0]
        if r == 'S' or r == 'N':
            break
print(f'O total de pessoas que foram cadastradas foi: {totpes}')
print(f'As pessoas mais pesadas, pesando {maipes[0][1]} kg, foram: ')
for p in maipes:
    print(p[0], end=', ')
print()
print(f'As pessoas mais leves, pesando {menpes[0][1]} kg, foram:')
for k in menpes:
    print(k[0], end=', ')
