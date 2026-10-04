# Using if Statemens with Lists
requested_toppings=['mushroom','green. peeper','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping.title()}")
print('Finished ur pizza with requested toppings on it!')

print("\n")

req_topings=['mushroom','green peeper']
for req_topping in req_topings:
    if req_topping=='green peeper':
        print(f"Sorry we are out of {req_topping}")
    else:
        print(f"Adding {req_topping}")

print("\n")

# Checking list is empty or not 

reqes_toppings=[]
if reqes_toppings:              # NOTE : loop break's here it self bcz "eques_toppings return ---> FALSE"
    for reqes_topping in reqes_toppings:
        print(f"Adding {reqes_topping}")
    print("Finished adding your topping")
else:
    print("Are you sure you don't want any topping's!")

print("\n")

cars=[]
if cars:
    for car in cars:
        print(f"Your cars are {car}")
    print("Finished printing ur alll cars ")
else:
    print("No car in your garage!")

