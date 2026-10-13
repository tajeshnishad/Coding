# Flags
prompt = 'Tell me something, I will repeat it back to you.'
prompt +='\nEnter the messae to print : '

active = True
while active :
    message = input(prompt)

    if message != 'quit':
        print(message)
    else:
        active = False

print("\n")

# 1)Movie Ticket Pricing(age=based Flag)

prompt = '\nGive me yur age and i will tell your movie tkt price'
prompt += '\nPlease enter your age : '

active = True
while active == True :
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print(f"Your tkt is free of cost")
        elif 3 <= age < 12:
            print(f"Your tkt price is $10")
        elif 12 <= age <=100:
            print(f"Your tkt price is $15")

print("\n")

# 2)Pizza Topping Collector
prompts = 'enter "done" to stop adding toppings : '
toppings = []
ordering = True
while ordering:
    user_topping = input(prompts)
    if user_topping == 'done':
        ordering = False
    else:
        toppings.append(user_topping)
print(toppings)
for items in toppings:
    print(items)

print("\n")

# 3)Three=Strike Secrete Passcode
prompt = "Enter Passcode : "
secret_code = "python"
attempts = 0
system_active = True

while system_active:
    user_code = input(prompt)
    if user_code == secret_code:
        print(f"Welcome! Access granted.")
        system_active = False
    else:
        attempts += 1
        print(f"Incorrect! Attempts used : {attempts}/3")
        if attempts == 3:
            print(f"Too many wrong attempts! System locked.")
            system_active = False