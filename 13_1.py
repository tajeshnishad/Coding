# Passing arguments
def describe_pet(animal_type,petname):
    print(f"\nI have a {animal_type.title()}")
    print(f"Name of my pet is {petname.title()}")

describe_pet('hamster','harry')

print("\n")

# taking multiple arguments 
def person_frnd(person_name,friend_name):
    print(f"\nName of the person is {person_name.title()}")
    print(f"Name of {person_name.title()}'s friend is {friend_name.upper()}")

person_frnd('tajesh','naveen')
person_frnd('bharat','akash')

print("\n")

# keryword arguments
def brothers(person_1,person_2):
    print(f"{person_1.title()} and {person_2.title()} are both brothers")
brothers(person_2 = 'akash',person_1 = 'bharat')

print("\n")

# defaut value
def pets(pet_name,pet_type = 'Dog'):
    print(f"\nYour {pet_type.title()}'s home name is {pet_name.title()}")
pets(pet_name='guddu')
pets(pet_type='cat', pet_name='billu')
# pets('bat','biddu')       NOTE : arguent placement order
# pets('cat') 