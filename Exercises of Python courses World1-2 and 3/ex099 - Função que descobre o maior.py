from time import sleep


def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    p = m = int(0)
    for c in num:
        print(c, end=" ")
        sleep(0.5)
        if p == 0:
            m = c
        else:
            if m < c:
                m = c
        p += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


maior(1, 5, 7, 15, 0)
maior(18, 35, 105)
maior()
