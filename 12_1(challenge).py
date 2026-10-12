# 1)coutdown time
countdown = 10
while countdown >= 1:
    print(countdown)
    countdown = countdown - 1
print('Liftoff!!')

print("\n")

current_number = 1
while current_number <= 20:
    if current_number % 2 == 0:
        print(f"Even number = {current_number}")
    else:
        print(f"Odd number = {current_number}")
    current_number += 1

print("\n")

# 3)Pizza Toppings
topping = 'now enter the pizza topping you want'
topping += '\nplease give the topping name : '
name = ' '
while name != 'quit':
    name = input(topping)
    print(f"you want pizza topping as  -> {name.lower()}")

# 4)Running distance logger
# total_distance = 0.0
# prompt = 'Enter run distance in km : '
# total_distance = input(prompt)
# if total_distance == 'done':
#     prompt = str(prompt)
# else:
#     prompt = float(prompt)
#     # while total_distance != 'done':
#     #     print(f"Total distance you have ran is : {total_distance}")