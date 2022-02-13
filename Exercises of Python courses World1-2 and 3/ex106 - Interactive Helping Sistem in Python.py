def minisistema(a):
    from time import sleep
    if a != 'FIM':
        print('\033[0;97;44m~' * (34 + len(a)))
        print(f'  ACESSANDO O MANUAL DO COMANDO "{a}"')
        print('~' * (34 + len(a)))
        sleep(1)
        print('\033[0;37;107m', end='')
        help(a)
    else:
        print('\033[0;97;41m~' * 13)
        print('  ATE LOGO!')
        print('~' * 13)
    sleep(1)


funcsis = str('')
while funcsis != 'FIM':
    print('\033[0;97;42m~' * 30)
    print(f'{"SISTEMA DE AJUDA DO PyHELP":^30}')
    print('~' * 30)
    funcsis = str(input('\033[mFunção ou Biblioteca > ')).strip()
    if funcsis in 'fimfterminarencerrarfinalizarpararprogramaTERMINARENCERRARFINALIZARPARARPROGRAMA':
        funcsis = 'FIM'
    minisistema(funcsis)
