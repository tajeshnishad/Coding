from electric_car import Elecrtic_car as EV
from car import Car

my_car = EV('mahindra','BE-6',2025)
print(my_car.get_descriptive_name())
my_car.readodometer()
my_car.battery.battery_size = 65
my_car.battery.describe_battery()
my_car.battery.get_range()

print("\n")

my_defender = Car('land-rover','defender',2025)
print(my_defender.get_descriptive_name())