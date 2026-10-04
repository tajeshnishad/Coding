# Using MULTIPLE LISTS
available_toppings=('mushroom','olives','green peeper','pepperoni','pinpple','extra cheese')
requested_toppings=['mushroom','french fries','extra cheese']

for reuested_topping in requested_toppings:
    if reuested_topping in available_toppings:
        print(f"Adding {reuested_topping}")
    else:
        print(f"Sorry! {reuested_topping} is not availabe.")
print("Finished making Your Pizza ")