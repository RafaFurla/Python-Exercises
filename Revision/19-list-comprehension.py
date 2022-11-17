from random import randint
cubes = [(i ** 3) for i in range(0, 5, 1)]
print(cubes)
randomic = [randint(0, 20) for i in range(10) if i % 2 == 0]
print(randomic)

