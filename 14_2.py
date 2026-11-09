class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car {self.odometer_reading} miles on it.")

    def update_odometer_reading(self,milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    def read_odometer_ev(self):
        super().read_odometer(self)

my_leaf = Electric_Car('mahindra','XE-9E',2025)
print(my_leaf.get_descriptive_name())
my_leaf.read_odometer()