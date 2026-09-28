fav_players=['dhoni','kholi','naveen','sonyhase','luis hamilton']
print(fav_players[:3])
print(fav_players[3:])

print('\n')

print('three item from middle of the list are :')
print(fav_players[1:-1])

print('\n')

print('Last 3 items in the list are : ')
print(fav_players[2:])

print('\n')
print('\n')

my_pizzas=['capricon','sweetcorn','mania','doble cheese','chicken cheese']
frnd_pizzas=my_pizzas[:]
my_pizzas.append('macroni')
frnd_pizzas.append('dracnoi')
print(my_pizzas[:])
print('\n')
frnd_pizza=[]
for frnd_pizz in frnd_pizzas:
    frnd_pizza.append(frnd_pizz)
print(frnd_pizza)

print('\n')

for my_pizz in my_pizzas:
    print(my_pizz)

print('\n')

for frnd_piz in frnd_pizzas:
    print(frnd_piz) 