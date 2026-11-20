class Restraunt:
    def __init__(self,restraunt_name,cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type

    def describe_restraunt(self):
        print(f"Restraunt name: {self.restraunt_name.title()}\n"
              f"Cuisine type: {self.cuisine_type.title()}")

    def open_restraunt(self,status='open'):
        self.status = status
        print(f"{self.restraunt_name.title()}, is currently {self.status.upper()}!")

