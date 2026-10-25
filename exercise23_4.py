# 1) Sandwich
def items_on_sandwich(*items):
    item = list(items)
    print(f"\nList of items persons want on their sandwich:")
    for thing in item:
        print(f"- {thing.title()}")

items_on_sandwich('Paneer', 'Green Chutney', 'Cucumber', 'Tomato')
items_on_sandwich('Grilled Chicken', 'Mayonnaise', 'Lettuce', 'Cheddar Cheese')
items_on_sandwich('Boiled Egg', 'Black Pepper', 'Butter', 'Spinach')

print("\n")

# 2) User Profile
def build_profile(first,last,**user_info):
    user_info['f_name'] = first.title()
    user_info['l_name'] = last.title()
    return user_info

user_profile = build_profile('Naveen','kumar',location = 'Secunderabad',field = 'B.Pharma')
print(user_profile)

print("\n")

# 3) Cars
def cars_info(manufracturer,model_name,**more_info):
    more_info['Manufracture'] = manufracturer.title()
    more_info['Model Name'] = model_name.title()
    return more_info

car = cars_info('suburu','outback',color = 'blue',tow_package = True)
print(car)