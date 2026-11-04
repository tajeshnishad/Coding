# Creating a dog class 
class Dog:
    def __init__(self,name,age):
        """initializa name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulates a dog sitting in response to a command"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Stimulate a rolling over in resopnse to a command."""
        print(f"{self.name.title()} rolled over!")

my_dog_1 = Dog('Willi',6)
print(f"My dog's name is {my_dog_1.name}")
print(f"My dog's age is {my_dog_1.age}")
my_dog_1.sit()

print("\n")

my_dog_2 = Dog('mitthu',12)
print(f"My 2nd pet's name is {my_dog_2.name.title()}")
print(f"My@nd pet's age {my_dog_2.age} yrs old.")
my_dog_2.roll_over()
my_dog_2.sit()

print("\n")

class Math_helper:
    def square(num):
        return num*num

num_square = Math_helper()
# print(num_square.square(12))
print(Math_helper.square(23))