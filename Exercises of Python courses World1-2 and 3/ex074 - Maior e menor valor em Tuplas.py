from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
me = n[0]
ma = n[0]
for c in n:
    if c < me:
        me = c
    if c > ma:
        ma = c
print(f'A tupla sorteada é {n}')
print(f'O maior número da tupla é {ma} e o menor é {me}')
# Outra forma de fazer o maior e o menor são com as seguintes funcionalidades:
print(f'O maior número da tupla é {max(n)} e o menor é {min(n)}')
