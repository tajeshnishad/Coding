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