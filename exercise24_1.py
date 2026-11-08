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
restraunt_1.set_number_served()

restraunt_2 = Restauraunt('bihari dabha','indian')
restraunt_2.describe_restraunt()
restraunt_2.open_restraunt()
restraunt_2.increment_number_served(1)
restraunt_2.set_number_served()