# Passing a list 
def greet_users(names):
    for name in names:
        msg = f"\nHello {name.title()}!"
        print(msg)

username = ['minal','ikku','kabir','naveen']
greet_users(username)

print("\n")

# Modifying a list in a function 

# # 1)making it without functions
unprinted_designs = ['phone case','robot pendent','dodecahedron']
compleated_models = []

print(f"Unprinted design are :")
for unprinted in unprinted_designs:
    print(unprinted.title())

for unprinted_design in unprinted_designs:
    compleated_models.append(unprinted_design.title())

print("\nCompleted designs are : ")
for completed_design in compleated_models:
    print(completed_design)

# 2)making it using functions
def print_model(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_desgn = unprinted_designs.pop()
        print(f"Printing model : {current_desgn.title()}")
        completed_designs.append(current_desgn)

def show_completed_models(completed_designs):
    print("\nThe following models have been printed: ")
    for competed_model in completed_designs:
        print(competed_model.title())

unprinted_model = ['phone case','robot pendent','dedecahedron']
completed_model = []

print_model(unprinted_model,completed_model)
show_completed_models(completed_model)