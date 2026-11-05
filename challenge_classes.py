class Smartphone:
    def __init__(self,brand,model_name,storage_gb,battery_mah):
        self.brand = brand
        self.model_name = model_name
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah

    def battery_status(self,current_battery):
        self.current_battery = current_battery

    def get_specs(self):
        return f"\nDevice: {self.brand.title()} {self.model_name} ({self.storage_gb})GB | Battery Capacity: {self.battery_mah}\nBattery Alert: {self.brand} {self.model_name} is at {self.current_battery}% battery remaining.\n"

smart_phone_1 = Smartphone('apple','iphone 14 pro max',256,3274)
smart_phone_1.battery_status(85)
print(smart_phone_1.get_specs())

smart_phone_2 = Smartphone('Samsung','Galaxy S24 Ultra',512,5000)
smart_phone_2.battery_status(42)
print(smart_phone_2.get_specs())