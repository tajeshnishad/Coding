# Challenge : Case-Insensitive Username Check (.lower() & in)
# Let's test handling user accounts and casing differences.
# Setup:
# Python
# current_users = ['Admin', 'John', 'Sarah', 'Alex', 'Mike']
# new_users = ['sarah', 'CHRIS', 'mike', 'Emma']
# Task:
# Create a new list current_users_lower containing all names from current_users converted to lowercase (using a loop or list comprehension).
# Loop through new_users:
# If the lowercase version of the new username is already in current_users_lower, print: "Sorry, <username> is already taken. Choose another name."
# Otherwise, print: "Great, <username> is available!"
# After checking all names, print: "All new usernames processed."


current_users = ['Admin', 'John', 'Sarah', 'Alex', 'Mike']
new_users = ['sarah', 'CHRIS', 'mike', 'Emma']
current_user=[]
for crnt_user in current_users:
    current_user.append(crnt_user.lower())
print(current_user)
for new_user in new_users:
    if new_user.lower() in current_user:
        print(f'Sorry, {new_user} is already taken. Choose another name.')
    else:
        print(f"Great, {new_user} is availabe.")