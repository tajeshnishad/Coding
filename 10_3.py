# Using multipe elif Blocks
age=12
if age<4:
    price=0
elif age<18:
    price=20
elif age<65:
    price=40
else:
    price=20
print(f"Your's admission fee is ${price}.")

print('\n')

# Omitting the else block
age=64
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"Your's admission cost is ${price}")