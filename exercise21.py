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