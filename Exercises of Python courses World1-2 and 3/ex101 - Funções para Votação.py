import datetime


def voto(a=0):
    """ A função voto calcula se o usuário tem idade para votar.
    :param a: ano de nascimento do usuário
    :return: essa função não retorna valores."""
    from datetime import datetime
    b = datetime.now().year - a
    if b < 16:
        print(f'Com {b} anos: NÃO VOTA!')
    elif 16 <= b < 18 or b >= 70:
        print(f'Com {b} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {b} anos: VOTO OBRIGATÓRIO!')


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
