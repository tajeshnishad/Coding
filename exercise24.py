# Resraunt 
class Restraunt:
    def __init__(self,restraunt__name,coisne__type):
        self.restraunt_name = restraunt__name
        self.coisine_type = coisne__type
        print(f"{self.restraunt_name.title()}")
        print(f"{coisne__type.title()}")

    def describe_restraunt(self):
        return f"{self.restraunt_name.title()} serves {self.coisine_type.title()}"

    def restraunt_status(self,status):
        return f"{self.restraunt_name.title()} is {status.upper()}!"

restraunt_1 = Restraunt('The rusty spoon','italine')
print(restraunt_1.describe_restraunt())
print(restraunt_1.restraunt_status('open'))

print("\n")

# Car Dealership Garage
class Car:
    def __init__(self,brand,model,year):
        self.car_brand = brand
        self.car_model = model
        self.car_year = year

    def get_car_info(self):
        return f"\nVehicle: {self.car_year} {self.car_brand.title()} {self.car_model.title()}"

    def test_drive_mode(self,mode):
        if mode.lower() == 'eco':
            return f"Status: The {self.car_year} {self.car_brand} {self.car_model} is driving quitely in {mode.upper()} mode!"
        elif mode.lower() == 'sport':
            return f"Status: The {self.car_year} {self.car_brand} {self.car_model} is driving fast in {mode.upper()} mode!"
        else:
            return f"Status: The {self.car_year} {self.car_brand} {self.car_model} is roaring in {mode.upper()} mode!"

car_1 = Car('nissan','gt-r','2024')
print(car_1.get_car_info())
print(car_1.test_drive_mode('Track'))

car_2 = Car('maruti','jimmy','2023')
print(car_2.get_car_info())
print(car_2.test_drive_mode('off-road'))

car_3 = Car('honda','civic','2021')
print(car_3.get_car_info())
print(car_3.test_drive_mode('eco'))

print("\n")

# Users
class Users:
    def __init__(self,first_name,last_name):
        self.f_name = first_name
        self.l_name = last_name

    def user_profile(self,usernme,email,location):
        self.username = usernme
        self.email = email
        self.location = location

    def describe_user(self):
        return f"User Profile:\n\tName: {self.f_name.title()} {self.l_name.title()}\n\tUsername: {self.username}\n\tEmail: {self.email}\n\tLocation: {self.location.title()}\nWelcome back, {self.f_name.title()}!\n"

user_1 = Users('alex','hunter')
user_1.user_profile('ahunter99','alex@example.com','berline')
print(user_1.describe_user())

user_2 = Users('maya','lin')
user_2.user_profile('mlin_dev','maya@example.com','tOkYo')
print(user_2.describe_user())