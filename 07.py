cars=['mahindra','tata','land rover','jlr','bmw']

# adding element to the list
# syntax --> cars.append()
print(cars)
cars.append('BYD')
print(cars)
cars.append('suzuki')
print(cars)
print('\n')


# removing/deleting elements from car
# syntax --> del list_name(index_no.)
print(cars)
del cars[0]
print(cars)
del cars[-1]
print(cars)
print('\n')

# modifing/overwritting list
print(cars)
cars[0]='mercedes'
print(cars)
cars[-2]='Rolls Royce'
print(cars)
print('\n')
