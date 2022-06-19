def double(funcao):
    def wrap(a, b):
        doubling = 2 * funcao(a, b)
        return doubling
    return wrap


@double
def add(x, y):
    return x + y


print(add(2, 5))
