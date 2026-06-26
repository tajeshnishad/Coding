bicycles=['trek','huge','atlas','specialized']
#index no.[  0  , 1    ,  2    ,     3       ]
#                   OR
#index no.[  -4 , -3   ,  -2   ,     -1      ]
print(bicycles)
print(bicycles[0])
print(bicycles[3].title())
print(bicycles[2].upper())
print(bicycles[-1])         #---------> always prints the last element of the list
print(bicycles[-2])
print(f'My fav. Bicycle is {bicycles[-2].title()}')