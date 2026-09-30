# If Statements(EQUALITY CHECKING)

cars=['audi','bmw','mahindra','suzuki']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n')

car='BMW'
print(car=='BMW')           #NOTE : TRUE

print('\n')

car='BMW'
print(car=='bmw')           #NOTE : FALSE

print('\n')

cars='audi'
print(cars=='BMW')

print('\n')

cars_='cadilack'
print(cars_.upper()=='CADILACK')
print(cars_)