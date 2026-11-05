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

print("\n")

# Challenge 2: Flight Booking Ticket
class Flight:
    def __init__(self,flight_number,departure_city,arrival_city,seat_number):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.seat_number = seat_number

    def get_boarding(self):
        return f"\nBoarding Pass: Flight {self.flight_number.upper()} from {self.departure_city.title()} to {self.arrival_city.title()} | Seat : {self.seat_number.upper()}"

    def flight_announcement_status(self,status):
        return f"Announcement: Flight {self.flight_number.upper()} is now {status.upper()}!"

flight_1 = Flight('6e-204','delhi','mumbai','14A')
print(flight_1.get_boarding())
print(flight_1.flight_announcement_status('boarding'))

flight_2 = Flight('ai-801','bengaluru','chennai','22f')
print(flight_2.get_boarding())
print(flight_2.flight_announcement_status('delayed'))

print("\n")

# Challenge 3: Gamer Profile
class GamerProfile:
    def __init__(self,gamer_tag,favourite_game,rank,hours_played):
        self.gamer_tag = gamer_tag
        self.favourite_game = favourite_game
        self.rank = rank
        self.hours_played = hours_played

    def show_profile(self):
        return (f"\nGamer Profile :\n"
               f"\tGamerTag: {self.gamer_tag}\n"
               f"\tGame: {self.favourite_game.title()}\n"
               f"\tRank: {self.rank.title()}\n"
               f"\tHours: {self.hours_played} hrs")

    def invite_to_party(self,host_name):
        return(f"{self.gamer_tag} was invited to a party by {host_name}!")

gamer_1 = GamerProfile('ShadowStrike','valorent','diamond',450)
print(gamer_1.show_profile())
print(gamer_1.invite_to_party('Phoenix'))

gamer_2 = GamerProfile('SpeedDemon','Forza horizen 5','Master',180)
print(gamer_2.show_profile())
print(gamer_2.invite_to_party('Nitro'))

print("\n")

class Workout:
    def __init__(self,exercise_name,sets,reps,weight_kg):
        self.exercise_name = exercise_name
        self.sets = sets
        self.reps = reps
        self.weight_kg = weight_kg

    def get_exercise_details(self):
        return (f"\nExercise: {self.exercise_name.title()}"
                f" | Routine: {self.sets} sets X {self.reps} reps @ {self.weight_kg} kg")

    def total_volume(self):
        volume = self.sets*self.reps*self.weight_kg
        return f"Total Volume Lifted: {volume} kg"

workout_1 = Workout('benchpress',4,8,70)
print(workout_1.get_exercise_details())
print(workout_1.total_volume())

workout_2 = Workout('barbell squat',3,10,90)
print(workout_2.get_exercise_details())
print(workout_2.total_volume())