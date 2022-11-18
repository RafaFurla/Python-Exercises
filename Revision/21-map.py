def addfive(x):
    return x + 5


a = [i for i in range (0, 6, 1)]
print(a)
print("map")
b = list(map(addfive, a))
print(b)
print("map with lambda function:")
c = list(map(lambda x: x**2, a))
print(c)

