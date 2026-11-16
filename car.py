# Importing classes
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

    def readodometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
            print(f"Your car has {mileage} on it.")
        else:
            print("You can'y roll back yor odometer!")

    def increament_odometer(self,miles):
        self.odometer_reading += miles