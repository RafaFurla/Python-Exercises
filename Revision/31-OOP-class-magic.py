class numberx:
    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        return 2 * self.value + other.value

    def __radd__(self, other):
        return self.value - other


x = numberx(8)
y = numberx(10)
z = int(2)
print(x + y)
print(y + x)
print(z + x)
print(z + y)

