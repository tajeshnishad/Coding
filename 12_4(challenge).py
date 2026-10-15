# 1)The Direct Conditional while
user = '\nEnter the cities you want to visit'
user += '\nEnter quit to stop : '
while user:
    city = input(user)
    if city == 'quit':
        user = False
    else:
        print(f"I'd love to go to {city.title()}")

print("\n")

# 2) Rental Car reservation
rental_prompt = 'Enter the brand of rental car theey would like to hire'
rental_prompt += '\nEnter "quit" to stop and print your request : '
rental_cars = [ ]
active = True
while active:
    cars = input(rental_prompt)
    if cars == 'quit':
        active = False
    else:
        rental_cars.append(cars)

print(rental_cars)

print("\n")

# 3)Movie Snak bar
snack_prompt = '\nPlease enter the product, whose price you want to know : '
snack_prompt += '\nEnter "quit" to stop : '
active = True
while active:
    item = input(snack_prompt)
    if item == 'quit':
        active = False
    else:
        if item == 'popcorn':
            print(f"{item.title()} cost is $5.")
        elif item == 'nachos':
            print(f"{item.title()} cost is $6.")
        elif item == 'soda':
            print(f"{item.title()} cost is $3.")
        else:
            print(f"{item.title()} not available.")

print("\n")

# 4)Fitness Goal Tracker
run_prompt = '\nEnter the distance ou have ran till now'
run_prompt += '\nEnter "stop" to furter adding on todays distance : '
goal_run = 15
total_run = 0
active = True
while active:
    km_run = input(run_prompt)
    if km_run == 'stop':
        active = False
    else:
        km_run = int(km_run)
        total_run += km_run
        if total_run < 15:
            print(f"Come on! Dude you are {goal_run-total_run} far to achive your goal run. Keep it up")
            
        else:
            print(f"Compeated your daily goal now take some rest")
            break

print("\n")

# 5)Sandwich Sho Limit
ingrediant_prompt = '\nEnter the ingrediants one by one'
ingrediant_prompt += '\nEnter "quit" to stop adding ingrediants : '
ingredinats_l = []
active = True
while active:

    ingredinats = input(ingrediant_prompt)

    if ingredinats == 'quit':
        active = False
    else:
        ingredinats_l.append(ingredinats)
        if len(ingredinats_l) == 4:
            active = False
for ingrediant in ingredinats_l:
    print(ingrediant.title())

print("\n")