def metade(preco=0):
    return preco/2


def dobro(preco=0):
    return preco * 2


def aumentar(preco=0, porcentagem=0):
    f = preco + (preco * (porcentagem / 100))
    return f


def diminuir(preco=0, porcentagem=0):
    f = preco - (preco * (porcentagem / 100))
    return f


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
