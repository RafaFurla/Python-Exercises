class cars:
    tires = 4
    doors = 4
    transmission = "automatic"
    

    def __init__(self, color, brand, hundred_time):
        self.color = color
        self.brand = brand
        self.hundred_time = hundred_time


civic = cars("white", "Honda", 7.9)
fusion = cars("grey", "Ford", 7.2)
ferrari = cars("red", "Fiat", 3)
ferrari.transmission = "manual"
ferrari.doors = 2
print(f"Quantity of doors in a Ferrari = {ferrari.doors}")
print(f"Quantity of doors in a Car = {cars.doors}")
print(f"Transmission type in a Ferrari: {ferrari.transmission}")
print(f"Transmission type in a Fusion: {fusion.transmission}")

