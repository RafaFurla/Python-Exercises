def test(x):
    i = x
    while i > 0:
        yield i
        i -= 1


print("Generator used to print numbers:")
for i in test(10):
    print(i)
print("Generator used to create lists:")
a = list(test(10))
print(a)

