def leiadinheiro(msg):
    while True:
        msg = str(input('Digite o preço: R$ ')).strip()
        if ',' in msg:
            msg = msg.replace(',', '.')
        temp = msg
        if '.' in temp:
            temp = temp.replace('.', '')
        if not temp.isdecimal() or msg.count('.') > 1:
            print(f'\033[0;31mERRO: "{msg}" é um preço inválido!\33[m')
        if temp.isdecimal() and 0 <= msg.count('.') <= 1:
            msg = float(msg)
            return msg


def leiaint2(inteiro=1):
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mO tipo de dado digitado não é um número inteiro!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o dado!\033[m')
            break
        else:
            print(f'\033[0;32mO número inteiro digitado é: {inteiro}\033[m')
            return inteiro


def leiafloat(real=1.0):
    while True:
        try:
            real = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[0;31mO tipo de dado digitado não é um número real\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o dado!\033[m')
            break
        else:
            print(f'\033[0;32mO número real digitado é: {real:.1f}\033[m')
            return real


def leiaintfloat(inteiro='none', real='none'):
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[0;31mO tipo de dado digitado não é um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o dado!\033[m')
            break
        else:
            break
    while True:
        try:
            real = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[0;31mO tipo de dado digitado não é um número real\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o dado!\033[m')
            break
        else:
            break
    return inteiro, real


def internetconnection(website):
    ''' A função vê se o website está acessível.
    :param website: Usuário entra com o website desejado
    :return: '''
    import urllib.error
    from urllib.request import urlopen
    try:
        urlopen(website, timeout=1)
    except urllib.error.URLError:
        print('\033[0;31mInternet Desconectada!')
        return False
    except ValueError:
        print('\033[0;31mEndereço Website digitado errado ou inválido!')
    else:
        print('\033[0;32mInternet Conectada! Site funcionando!')
        return True


'''   except Exception as error:
        print(error.__class__,
              error.__format__(),
              error.__cause__,
              error.__context__,
              error.args,
              error.__getattribute__(),
              error.with_traceback(),
              error.__annotations__,
              error.__delattr__(),
              error.__dict__,
              error.__dir__(),
              error.__eq__(),
              error.__hash__(),
              error.__init__(),
              error.__init_subclass__(),
              error.__ne__(),
              error.__new__(),
              error.__reduce__(),
              error.__reduce_ex__(),
              error.__repr__(),
              error.__setattr__(),
              error.__sizeof__(),
              error.__slots__,
              error.__str__(),
              error.__suppress_context__,
              error.__traceback__,
              error.__doc__,
              error.__module__)
'''
