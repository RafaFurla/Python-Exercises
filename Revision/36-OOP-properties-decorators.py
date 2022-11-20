class Cars:
    def __init__(self, brand):
        self._spec = ["Trasmission: manual", "4 tires"]
        while brand not in "HondaFordFiat":
            print("You must choose a valid brand: Honda, Ford or Fiat")
            brand = input("Enter with a valid brand: ")
        if brand in "HondaFordFiat":
            self.brand = brand


    @property
    def spec(self):
        return f"The specification of this car is {self._spec}"

    @spec.setter
    def spec(self, s):
        self._spec = [f"Transmition: {s[0]}", f"{s[1]} tires"]
    
    @spec.deleter
    def spec(self):
        del self._spec


civic = Cars("Volks")
print(civic.spec)
civic.spec = ("Automatic", 3)
print(civic.spec)
del civic.spec
print(civic.spec)
