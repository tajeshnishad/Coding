# Passing as arbitariry number of arguments
def make_pizza(*topping):
    print(topping)
make_pizza('peproni')
make_pizza('mushroom','chicken','green peeper')

print("\n")

def make_pizzas(*toppings):
    print("Toppings you will be getting on your pizza :")
    for toppin in toppings:
        print(toppin.title())
make_pizzas('peproni\n')
make_pizzas("mushroom",'green peeper','chicken','extra cheese\n')

print("\n")


