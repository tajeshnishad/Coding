# 1) Working with Lists
unconfirmed_user = ['naveen','anshul','kabir','ikku','naveen','minal','anshul']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    confirmed_user.append(current_user)

print(confirmed_user)
print(unconfirmed_user)
print(set(confirmed_user))

while 'anshul' in confirmed_user:
    confirmed_user.remove('anshul')

print(confirmed_user)
print(type(set(confirmed_user)))

print("\n")

# 2) Working with Dictionary
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name : ")
    response = input("\nWhich mountain would you like to climb someday? : ")

    responses[name] = response

    repeat = input("\nWouldd you let another person respond? (yes/no) : ")
    if repeat == 'no':
        break
    else:
        continue

print("---Poll Results---")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")