class Car:
    _tires = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def _factor(self):
        if self.brand == "Honda":
            self.factor = 0.07
        elif self.brand == "Fiat":
            self.factor = 0.05
        else:
            self.factor = 0.08
        return self.factor

    def __breakfactor(self):
        if self.brand == "Honda":
            self.factor = 0.1
        elif self.brand == "Fiat":
            self.factor = 0.15
        else:
            self.factor = 0.2
        return self.factor

    def aceleration(self, fvel):
        time = self._factor() * fvel
        return f"{time:.10} seconds to reach the velocity of {fvel}km/h"
    
    def deaceleration(self, ivel):
        time = self.__breakfactor() * ivel
        return f"{time:.10} seconds to break the car from {ivel}km/h to zero km/h"


honda = Car("Honda", "Civic")
print(honda.brand)
print(honda.model)
print(honda.aceleration(100))
print(honda.deaceleration(100))
print(honda._factor())  # Hiding method
print(honda._Car__breakfactor())  # manglind the name to avoid confusion.

