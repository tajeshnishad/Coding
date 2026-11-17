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

class Battery:
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150

        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class Elecrtic_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()