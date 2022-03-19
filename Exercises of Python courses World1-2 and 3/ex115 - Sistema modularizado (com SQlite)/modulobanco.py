def principal():
    from time import sleep
    while True:
        visual('MENU PRINCIPAL')
        print('\033[0;33m1\033[m - \033[0;34mVer pessoas cadastradas\033[m')
        print('\033[0;33m2\033[m - \033[0;34mCadastrar nova Pessoa\033[m')
        print('\033[0;33m3\033[m - \033[0;34mSair do Sistema\033[m')
        while True:
            try:
                opcao = int(input('\033[0;32mSua Opção: \033[m'))
            except (ValueError, TypeError):
                print('\033[0;31mPor favor, digite um número inteiro válido!\033[m')
                opcao = 4
            except KeyboardInterrupt:
                print('\033[0;31mO usuário preferiu não digitar uma opção!')
                opcao = 4
            if opcao != 1 and opcao != 2 and opcao != 3:
                print(f'\033[0;31mEssa não é uma opção válida! Digite 1, 2 ou 3.\033[m')
            else:
                break
        if opcao == 1:
            vercadastro()
            sleep(2)
        if opcao == 2:
            cadastronovo()
            sleep(2)
        if opcao == 3:
            sleep(1)
            visual('Saindo do Sistema... Até logo!')
            break


def cadastronovo():
    import sqlite3 as lite
    conexao = lite.connect('clientes.db')
    visual('NOVO CADASTRO')
    valores = [str(input('Insira o nome do cliente: '))]
    while True:
        try:
            idade = int(input('Insira a idade do cliente: '))
        except (ValueError, TypeError):
            print('\033[0;31mPor favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar uma opção!')
        else:
            valores.append(idade)
            break
    with conexao:
        cur = conexao.cursor()
        query = 'INSERT INTO Clientes (nome, idade) VALUES(?, ?)'
        cur.execute(query, valores)
    print(f'Novo Registro de {valores[0]} adicionado.')
    valores.clear()


def vercadastro():
    import sqlite3 as lite
    conexao = lite.connect('clientes.db')
    visual('PESSOAS CADASTRADAS')
    cur = conexao.cursor()
    cur.execute('SELECT * FROM Clientes')
    for c, v in enumerate(cur.fetchall()):
        print(f'{v[0]:<29}{v[1]:<3}anos    ')


def visual(msg):
    msg = str(msg)
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)
