message = input('Tell me something ,I will repeat it baack to you :')
print(message)

print("\n")

name = input("Enter your name : ")
print(f"Hello, {name.title()}")

print("\n")

prompt = "If you can share your name, we can personalise the message for you"
prompt += ("\nPlease enter your name : ")
name  = input(prompt)
print(f"Helo!, {name}")

print("\n")

age = input("How old are you : ")
print(f"Your age is : {age}")

print("\n")

friend = input("Tell the name of your Best Friend : ")
print(f"Your Best Friend name is : {friend.title()}")

print("\n")

age = input('plz write down your name : ')
print(f"your age is : {age}")
print(age >= 21)

print("\n")

age = input("Enter your name : ")
print(f"Your age is : {age}")
age = int(age)
print(age >= 18)

print("\n")

name = input("enter your name : ")
f_name = input("enter your friends name : ")
print(f"your name is {name.title()}")
print(f"your friend's name is {f_name.title()}")
if f_name.lower() == 'naveen':
    print(f"{name.title()}'s best-friend is {f_name.title()} ")

print("\n")

height = input(f"How tall are you in inches : ")
height = int(height)

if height >= 40 :
    print(f"Your are eligible to ride")
else:
    print("Sorry you can't ride")

print("\n")

print(4%5)
print(11%9)
print(11%5)

print("\n")

number_1 = input("Enter your number : ")

if number_1 % 2 == 0:
    print(f"Given number are even") 
else:
    print("Given number is odd")