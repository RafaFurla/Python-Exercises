def fatorial(n=1, show=False):
    """→ Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n. """
    f = int(1)
    for c in range(n, 0, -1):
        f *= c
        if show and c != 1:
            print(f'{c}', end=' x ')
        if show and c == 1:
            print(f'{c}', end=' = ')
    return f


# Programa principal
print('-' * 30)
k = fatorial(10, True)
print(k)
help(fatorial)
