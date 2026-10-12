# 1) Rental Car
car = input("What kind of rentel car you would like to have : ")
print(f"Let me see, if I find you a {car.title()}")

print("\n")

# 2)Reastrount Seating
number = input("Number of people's with you in dinner : ")
number = int(number)

if number >= 8:
    print("You will have to wait for a table")
else:
    print("Table is ready")

print("\n")

# 3)Multiple of ten
number = input("Enter a number : ")
number  = int(number)

if number % 10 == 0 :
    print(f"Number is a multiple of 10")
else:
    print(f"Number is not a multiple of 10")

