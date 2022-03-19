def metade(preco, formatar=False):
    if formatar:
        return moeda(preco/2)
    else:
        return preco/2


def dobro(preco, formatar=False):
    if formatar:
        return moeda(preco * 2)
    else:
        return preco * 2


def aumentar(preco, porcentagem, formatar=False):
    f = preco + (preco * (porcentagem / 100))
    if formatar:
        return moeda(f)
    else:
        return f


def diminuir(preco, porcentagem, formatar=False):
    f = preco - (preco * (porcentagem / 100))
    if formatar:
        return moeda(f)
    else:
        return f


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, percentmais=0, percentmenos=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(preco):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(preco, True):<10}')
    print(f'{"Metade do Preço:":<20}{metade(preco, True):<10}')
    print(f'{percentmais:<3}{"% de aumento:":<17}{aumentar(preco, percentmais, True):<10}')
    print(f'{percentmenos:<3}{"% de aumento:":<17}{diminuir(preco, percentmenos, True):<10}')
    print('-' * 30)
