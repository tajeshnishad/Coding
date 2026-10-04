# 1) Helo Admin
user_names=['sunnyxyx','kbirdnd','admin','ikkubreaker','minall']
for user_name in user_names:
    if user_name=='admin':
        print(f"Hello admin would you like see the status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again!")

print("\n")

# 2) No Users
users=['sunny','naveen','kabir']
users.remove('sunny')
users.remove('naveen')
users.remove('kabir')
print(users)
if users:
    for user in users:
        print(f"we have some users with the user name {user}")
else:
    print(f"The list is empty we need to find some users!")

print("\n")

# 3) Checking Usernames

current_usernames=['chocO121','sunnyDxd','naVeengalaxy','xxXy','knightRider']
new_usernames=['kshan1976','choco121','Naveengalaxy','xxy','minall']
current_user_lower=[]
for current_user in current_usernames:
    current_user_lower.append(current_user.lower())
print(current_user_lower)

for new_username in new_usernames:
    if new_username.lower() in current_user_lower:
        print(f"Username {new_username} alreay exist! Please use different username")
    else:
        print(f"Good, you can use your username as {new_username}")

print("\n")

# 4) Ordinal Numbers
ordinal_numbers=[1,2,3,4,5,6,7,8,9]
for ordinal_number in ordinal_numbers:
    if ordinal_number==1:
        print(f"{ordinal_number}st")
    elif ordinal_number==2:
        print(f"{ordinal_number}nd")
    elif ordinal_number==3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")