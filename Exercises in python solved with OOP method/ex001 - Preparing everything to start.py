class START:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return self.value + other.value


class MSG:
    def __init__(self, msg):
        self.msg = str(msg)

    def prt(self):
        return print(f"{'=' * (len(self.msg) + 2)}\n{self.msg:^{(len(self.msg) + 2)}}\n{'=' * (len(self.msg) + 2)}")


colors = {'clean': '\033[m', 'blue': '\033[36m', 'green': '\033[32m'}
MSG('REVEALING THE CLASS OF THE OBJECTS').prt()
n1 = START(input('Input a integer number: '))
n2 = START(input('Input other integer number: '))
s = START(n1 + n2)
print(f'The sum between {colors["green"]}{n1.value}{colors["clean"]} and {colors["green"]}{n2.value}{colors["clean"]} is equal to {colors["blue"]}{s.value}{colors["clean"]}')
print(f'{colors["blue"]}{type(n1)}{colors["clean"]}')
print(f'{colors["blue"]}{type(n2)}{colors["clean"]}')
print(f'{colors["blue"]}{type(s)}{colors["clean"]}')
