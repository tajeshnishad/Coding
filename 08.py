cars=['bmw','mahindra','tata','audi']
print(f'{cars},ORIGINAL')

print(f'{sorted(cars)},temperorly sorted')

print(f'{cars}see,ORIGINAL is printed here again!')

cars.reverse()
print(f'{cars},printed original in reverse')

cars.sort()
print(f'{cars},permenantly sorted in alphabetical order')

cars.sort(reverse=True)
print(f'{cars},permanently sorted in reverse order')

print(f'{cars},Lets see !,how is the cars list is arranged over here at fianl step')
print(len(cars))