class Cars:
    doors = 4
    tires = 4
    transmission = "automatic"
    
    def __init__(self, model, color, brand, hundredtime):
        self.model = model
        self.color = color
        self.brand = brand
        self.hundredtime = hundredtime


class Ferrari(Cars):
    doors = 2
    transmission = "Manual"
    
    def canrace(self):
        if self.hundredtime < 3.5:
            return "Yes! This car can race!"
        else: 
            return "No! This car can't race!"


f40 = Ferrari("f40", "red", "Fiat", 3.1)
coupe = Ferrari("166_Inter_Coupe", "black", "Fiat", 11)
civic = Cars("Civic", "white", "Honda", 7.9)
print(f"Quantity of doors:\nCivic {civic.doors}\nFerrari F40:{f40.doors}\nFerrari 166 Inter Coupe: {coupe.doors}")
print(f"Type of transmission:\nCars in general: {Cars.transmission}\nCivic: {civic.transmission}\nFerrari F40: {f40.transmission}\nFerrari 166 Inter Coupe: {coupe.transmission}")
print(f"Can F40 race? {f40.canrace()}")
print(f"Can Ferrari 166 Inter Coupe race? {coupe.canrace()}")

