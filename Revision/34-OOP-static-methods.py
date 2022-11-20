class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @staticmethod
    def aceleration(fvel):
        time = 0.75 * fvel
        return f"{time:.10} seconds to reach the velocity of {fvel}km/h"


civic = Car("Honda", "Civic-V2")
print(f"Vehicle brand: {civic.brand}\nVehicle model: {civic.model}\nVehicle aceleration: {civic.aceleration(100)}")

