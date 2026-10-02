# If-elif-else statements 

age=23
if age>=18:
    print("Your are eligible to Vote!")
    print("Have you regitered to vote yet?")
else:
    print("You cannot vote, Sorry!")
    print("Please register to vote as soon as you turn 18")

print('\n')

person_age=18
if age<=4:
    print("free tkt to ammusment park")
elif 4<person_age<=18:
    print("your tkt fees is $25")
else:
    print("Your fees is $40")

print("\n")

per_age=23
if per_age<0:
    price=0
elif per_age<19:
    price=25
else:
    price=40
print(f"Your admission fees is ${price}.")