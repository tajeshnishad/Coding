def printing_model(argument_0,argument_1):
    print(f"\nThese is your argument - {argument_0}\n")
    print(f"\nThese is your argument - {argument_1}\n")

def pizza_info(size,*toppings):
    print(f"\nSize of the pizza is {size} and toppins in it are :")
    for topping in toppings:
        print(f"- {topping}")