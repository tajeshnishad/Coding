# Avoiding arguments error
def descibe_pet(pet_type,pet_name):
    print(f"\nYour {pet_type.title()}'s good name is {pet_name.title()}")
descibe_pet()

# o/p:
# Traceback (most recent call last):
#   File "/Users/tajeshnishad/VS code/Coding/13_2.py", line 3, in <module>
#     descibe_pet()
# TypeError: descibe_pet() missing 2 required positional arguments: 'pet_type' and 'pet_name'