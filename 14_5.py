# Instances as Attributes 
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = 30

    def fuel_capacity(self,fuel):
        self.fuel = fuel
        print(f"Fuel tank capacity of the car is {self.fuel}")

    def car_descrition(self):
        print(f"{self.model}\n{self.year}\n{self.make}\n{self.fuel}")

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size == 40:
            range =150
        elif self.battery_size == 65:
            range = 225
        print(f"Range of the car is {range}kms")

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

    def fuel_capacity(self):
        print(f"\nElcetric car's don't have fuel tank it has battery cpacity")

    def car_descrition(self):
        super().car_descrition()

my_leaf = Electric_car('nissan','my leaf',2024)
my_leaf.battery.get_range()
my_leaf.battery.describe_battery()
my_leaf.fuel_capacity()
my_leaf.car_descrition()
