# Overidding Methods from the Parents class 
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

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_capacity = 40

    def fuel_capacity(self):
        print(f"\nElcetric car's don't have fuel tank it has battery cpacity")

    def batery_capacity(self,batttery_size):
        self.battery_capacity = batttery_size
        print(f"Battery capacity of these car is {self.battery_capacity}")

    def car_descrition(self):
        print(f"{self.battery_capacity}")
        return super().car_descrition()


car_1 = Car('mahindra','bolero',2011)
car_1.fuel_capacity(30)
car_1.car_descrition()

car_2 = Electric_car('Mahindra','BE-6',2025)
car_2.fuel_capacity()
car_2.batery_capacity(55)
car_2.car_descrition()