# 9-6 Ice-Creamed Stand
class Restraunt:
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.served_number = 0

    def describe_restraunt(self):
        return (f"\nRestraaunt name: {self.name.title()}\n"
                f"Cuisine type: {self.cuisine_type.title()}")

    def restraut_status(self,status = 'close'):
        return f"{self.name.title()} is currently {status.upper()}!"

class IcecreamStand(Restraunt):
    def __init__(self,name,cuisine_type='Ice Cream'):
        super().__init__(name,cuisine_type)

    def describe_restraunt(self):
        return super().describe_restraunt()

    def restraut_status(self, status='close'):
        return super().restraut_status(status)

    def flavours(self,*flavours):
        print(f"\nAvailable flavours:")
        for flavour in flavours:
            print(f"-{flavour.title()}")


restraunt_1 = IcecreamStand('cool Scoops')
print(restraunt_1.describe_restraunt())
print(restraunt_1.restraut_status('open'))
restraunt_1.flavours('vanilla', 'chocolate', 'mango', 'butterscotch')

print("\n")

# 9-7. Admin
class User:
    def __init__(self,first_name,last_name,email,ph_number,location):
        self.f_name = first_name
        self.l_name = last_name
        self.email = email
        self.ph_number = ph_number
        self.location = location
        self.login_attempts = 0

    def describe_info(self):
        print(f"User Info:")
        return(f"-Full name: {self.f_name.title()} {self.l_name.title()}"
               f"\n-E mail: {self.email}"
               f"\n-Phone: {self.ph_number}"
               f"\n-Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello! Welcome back {self.f_name} {self.l_name}")

    def increment_login_attempts(self):
        self.login_attempts +=1
        print(f"Login attempts is: {self.login_attempts}")
        

    def reset_value(self):
        self.login_attempts = 0
        print(f"Login attempts have been reset to {self.login_attempts}")

class Admin(User):
    def __init__(self,first_name,last_name,email,ph_number,location):
        super().__init__(first_name,last_name,email,ph_number,location)
        self.privileges = []

    def show_privileges(self,*privileges):
        self.privileges = privileges
        print(f"\nAdministrator Privileges:")
        for privilege in privileges:
            print(f"-{privilege.title()}")


user_1 = Admin('vaibhav','nishad','vaibhav2005@gmail.com',9493830981,'Chhattisgarh')
print(user_1.describe_info())
user_1.greet_user()
user_1.show_privileges('can add post', 'can delete post', 'can ban user', 'can modify settings')