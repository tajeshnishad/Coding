from car import Elecrtic_car

my_car = Elecrtic_car('mahindra','BE-6',2025)
print(my_car.get_descriptive_name())
my_car.readodometer()
my_car.battery.battery_size = 65
my_car.battery.describe_battery()
my_car.battery.get_range()