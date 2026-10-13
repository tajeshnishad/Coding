# 1)Pizza Toppings:
prompt = 'Enter the toppings you want on your pizza : '
toppings = []
flag = True
while flag:
    topping = input(prompt)
    if topping == 'quit':
        flag = False
    else:
        toppings.append(topping)
print(toppings)
print(f"all these are your toppings on your pizza ")
for pizza in toppings :
    print(pizza.title())

print("\n")

age = 'Enter your age, we will tell your MOVIE TKT price by your age : '
flag = True
while flag :
    user_age = input(age)
    if user_age == 'quit':
        flag = False
    else:
        user_age = int(user_age)
        if user_age < 3:
            print('Ticket is free for you')
        elif 3 <= user_age <= 12:
            print('Ticket price is $10')
        elif user_age >= 12:
            print('Ticket price is $15')
        else:
            flag = False