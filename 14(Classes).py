# Creating a dog class 
class Dog:
    def __init__(self,name,age):
        """initializa name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Stimilates a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Stimulate a rolling over in resopnse to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willi',6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
