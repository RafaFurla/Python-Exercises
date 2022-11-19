class Cat:
    def __init__(self, color, legs=4):
       self.color = color
       self.legs = legs


    def isnormal(self):
        if self.legs==4:
            return "The cat is normal."
        else:
            return f"The cat is not normal because it has {self.legs} legs!"


felix = Cat("White", 4)
gargamel = Cat("Black", 3)
tom = Cat("Grey", 4)

print(felix.isnormal)
print(felix.isnormal())
print(Cat.isnormal(gargamel))
print(tom.color)
print(tom.legs)

