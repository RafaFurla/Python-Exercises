from utilidadesCeV.dado import internetconnection
coneccao = internetconnection('http://www.pudim.com.br/')
if coneccao:
    print('Consegui acessar o site Pudim com sucesso!\033[m')
if not coneccao:
    print('O Site Pudim não está acessível no momento.\033[m')
