# Defining attributes adn Mehods for the child class 
class Car:    #PARENT CLASS
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        print(f"\n{self.year} {self.model} {self.make}")

class Electeric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_capacity = 40

    def get_descriptions(self):
        print(f"\n{self.year} {self.model} {self.make} {self.battery_capacity}-kwh")

    def default_battery(self):
        print(f"This car has a {self.battery_capacity}-kwh battery.")

    def describe_battery(self,battery_capacity):
        print(f"This car has a {battery_capacity}-kwh battery.")

car_ev = Electeric_car('mahindra','BE-6',2025)
car_ev.get_descriptions()
car_ev.default_battery()
car_ev.describe_battery(23)