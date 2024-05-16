# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color


# Creating an instance of the Vehicle class
vehicle = Vehicle("Toyota", "Corolla")
vehicle.display_info()

print()

# Creating an instance of the Car class
car = Car("Toyota", "Corolla", "Red")
car.display_info()
