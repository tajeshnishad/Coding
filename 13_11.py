# mixing positional and arbitariary arguments
def make_pizza(size,*toppings,Default = None):
    print(f"\nSize of your pizza is {size}, toppings on it are:")
    for topping in toppings:
        print(topping.title())
    print(Default)

make_pizza(14,'peproni',Default = 'yay')
make_pizza(25,'extra cheese','green peeper','chicken','mushrooms',Default = 'dyumnn')
