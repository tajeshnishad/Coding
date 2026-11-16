from car import Car
my_new_car = Car('audi','a4',2025)
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 20
my_new_car.readodometer()
my_new_car.update_odometer(35)
