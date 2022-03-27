class MAMMALS:
    def __init__(self, milk=True, bodyhair=True, dioecious=True):
        self.milk = bool(milk)
        self.bodyhair = bool(bodyhair)
        self.dioecious = bool(dioecious)

    def jump(self):
        from random import random
        return random()

    def hdbreath(self):
        from random import random
        return random()


class CAT(MAMMALS):
    def __init__(self, name, milk=True, bodyhair=True, dioecious=True, legs=4, eyes=2, ears=2, tail=True):
        super().__init__(milk, bodyhair, dioecious)
        self.name = str(name)
        self.legs = legs
        self.eyes = eyes
        self.ears = ears
        self.tail = tail

    def catjump(self):
        return f'The jump of cat {self.name} reach {super().jump() * 1.5:.2f} meters'


class WHALE(MAMMALS):
    def __init__(self, name, milk=True, dioecious=False, bodyhair=False, eyes=2, tail=True):
        super().__init__(milk, bodyhair, dioecious)
        self.name = str(name)
        self.eyes = int(eyes)
        self.tail = bool(tail)

    def hdbreath(self):
        return f'The whale {self.name} holded breath for {super().hdbreath() * 138:.0f} minutes in last travel!'

    def whalejump(self):
        return f'The whale {self.name} just jumped {super().jump() * 15.24:.2f} meters out of water!'


bibi = CAT(name='Bibi')
willy = WHALE(name='Willy', eyes=1)
print(f"The name of gatinha do papai is: {bibi.name}")
print(bibi.catjump())
print(f"The name of the whale is: {willy.name}")
print(f"Willy has {willy.eyes} eye(s)")
print(willy.hdbreath())
print(willy.whalejump())
