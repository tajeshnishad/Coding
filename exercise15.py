# 1)Aline_color

alien_colors=['green','yellow','red','pink']
color_shot='blue'
if color_shot=='green' in alien_colors:
    print(f"player just earned 5 points")
if color_shot=='pink' in alien_colors:
    print((f"player just earned 0 points"))
else:
    print()

print('\n')

# 2) Aline_colors

alien_color='green'
if alien_color=='green' in alien_colors:
    points=5
else:
    points=10
print(f" player just earned {points} for shooting the {alien_color}!")

print("\n")

# 3) Alien_colors
aline_color='green'
if aline_color=='green' in alien_colors:
    points=5
elif aline_color=='yellow' in alien_colors:
    points=10
else:
    points=15
print(f"player earned {points} points!")

print("\n")

# 4) Stages of life
age=23
if age<2:
    print("Person is a Baby")
elif 2<=age<4:
    print("Person is a Toddler")
elif 4<=age<13:
    print("Person is a Kid")
elif 13<=age<20:
    print("Person is a Teenager")
elif 20<=age<65:
    print("Person is an Adult")
else:
    print("Person is and eleder")

print("\n")

# 5) Favorite_Fruit

fav_fruits=['apple','kiwi','watermelon','mango','black berry']
fav_fruit='black berry'
if fav_fruit=='apple'in fav_fruits:
    print(f"{fav_fruit.title()} is ur fav fruit!")
if fav_fruit=='kiwi'in fav_fruits:
    print(f"{fav_fruit.title()} is ur fav fruit!")
if fav_fruit=='wtermelon'in fav_fruits:
    print(f"{fav_fruit.title()} is ur fav fruit!")
if fav_fruit=='mango'in fav_fruits:
    print(f"{fav_fruit.title()} is ur fav fruit!")
if fav_fruit=='black berry'in fav_fruits:
    print(f"{fav_fruit.title()} is ur fav fruit!")

most_fav_fruits=fav_fruits[0:3]
print("My most favorite Fruits are:")
for most_fav_fruit in most_fav_fruits:
    print(most_fav_fruit.title())

fruit='mango'
if fruit=='banana' in fav_fruits:
    print(f"You really like {fruit.title()}")
if fruit=='kiwi' in fav_fruits:
    print(f"You really like {fruit.title()}")
if fruit=='watermelon' in fav_fruits:
    print(f"You really like {fruit.title()}")
if fruit=='mango' in fav_fruits:
    print(f"You really like {fruit.title()}")