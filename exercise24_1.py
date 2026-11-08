class Restauraunt :
    def __init__(self,restraunt_name,couisine_type):
        self.restraunt_name = restraunt_name
        self.cousine_type = couisine_type
        self.number_served = 0

    def describe_restraunt(self):
        return print(f"\nRestraunt Name: {self.restraunt_name.title()}"
                     f"\nCousine type: {self.cousine_type.title()}")

    def open_restraunt(self,status = 'close'):
        return print(f"Restraunt status: {status.upper()}")

    def increment_number_served(self,number_served):
        if number_served < self.number_served:
            number_served = self.number_served
            print(f"Number of customer's served: {number_served}")
        else: 
            self.number_served += number_served
            print(f"Number of customer's served: {number_served}")

    def set_number_served(self,number):
        self.number_served = number
        print(f"Total number of times served : {self.number_served}")


restraunt_1 = Restauraunt('the royal spice','indian')
restraunt_1.describe_restraunt()
restraunt_1.open_restraunt('open')
restraunt_1.increment_number_served(2)
# restraunt_1.set_number_served()

restraunt_2 = Restauraunt('bihari dabha','indian')
restraunt_2.describe_restraunt()
restraunt_2.open_restraunt()
restraunt_2.increment_number_served(1)
# restraunt_2.set_number_served()

# similar type 

# Challenge: Coffee Shop Order Tracker
class CoffeeShop:
    def __init__(self,shop_name,location):
        self.shop_name = shop_name
        self.location = location
        self.orders_completed = 0

    def describe_shop(self):
        return (f"Coffee Shop: {self.shop_name.title()}\n"
                f"Location: {self.location}")

    def shop_status(self,status):
        return (f"Status: {status.upper()}")

    def set_orders_completed(self,new_orders):
        if new_orders >= self.orders_completed:
            self.orders_completed = new_orders
        else:
            print(f"Cannot decrese the number of completed orders!")

    def increment_orders_completed(self,addittional_orders):
        if addittional_orders > 0:
            self.orders_completed += addittional_orders
            return self.orders_completed
        else:
            print(f"Addittional order must be greater than zero!")


shop = CoffeeShop('brew master', 'raipur')

shop.describe_shop()
shop.shop_status('open')
print(f"Orders completed: {shop.orders_completed}")
shop.orders_completed = 12
print(f"Orders completed: {shop.orders_completed}")

shop.set_orders_completed(30)
print(f"Orders completed: {shop.orders_completed}")
shop.increment_orders_completed(15)
print(f"Orders completed: {shop.orders_completed}")
shop.set_orders_completed(20)
shop.increment_orders_completed(-5)

print("\n")

# Login Attempts
class Users:
    def __init__(self,first_name,last_name,user_id,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.user_id = user_id
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFirst name: {self.first_name.title()}\n"
              f"Last name: {self.last_name.title()}\n"
              f"Email id: {self.email}\n"
              f"Location: {self.location.title()}")

    def greet_users(self):
        print(f"Hello!! \nWelcome back {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self,attempts):
        if attempts > self.login_attempts:
            self.login_attempts += attempts
        print(f"Login attempts of {self.first_name.title()} {self.last_name.title()} is {self.login_attempts}")

    def reset_login_attempt(self):
        if self.login_attempts >= 1:
            self.login_attempts = 0
        print(f"Login attempt has been reset to {self.login_attempts}")

user1 = Users('alex', 'hunter', 'ahunter99', 'alex@example.com', 'berlin')
user2 = Users('maya', 'lin', 'mlin_dev', 'maya@example.com', 'tokyo')

user1.describe_user()
user1.greet_users()
user1.increment_login_attempts(1)
user1.reset_login_attempt()

user2.describe_user()
user2.greet_users()
user2.increment_login_attempts(4)
user2.reset_login_attempt()