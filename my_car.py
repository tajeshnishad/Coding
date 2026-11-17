# importing Modules 
from car import Car
my_new_car = Car('audi','a4',2025)
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 20
my_new_car.readodometer()
my_new_car.update_odometer(35)

print("\n")

# Importing multiple classes from a module 
from car import Car,Elecrtic_car
my_bolero = Car('mahindra','bolero plus',2011)
print(my_bolero.get_descriptive_name())
my_ev = Elecrtic_car('mahindra','BE-6',2025)
print(my_ev.get_descriptive_name())
my_ev.battery.battery_size = 40
my_ev.battery.get_range()

print("\n") 
