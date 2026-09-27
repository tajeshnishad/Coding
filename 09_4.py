# SLICING

car=['lambo','jeep','mahindra','tata']
print(car[0])
print(car[0:3])

print('\n')

players=['naveen','kabir','ikku','sunny','sony']
print(players[1:])
print(players[1:4])

print('\n')

player=['sony','lewis','max','sunny','f1']
print(player[:3])
print(player[:-1])
print(player[-2:])

mobiles=['moto','apple','samsung','vivo','mi']
print("these are my first 4 mobile models in my list :")
for mobile in mobiles[:4]:
    print(mobile.title())