# Return Values
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

origina_name = get_formatted_name('tajesh','nishad')
print(origina_name)

print("\n")

def formatted_frnd_name(fi_name,las_name):
    friends_full_name = (f"{fi_name} {las_name}")
    return friends_full_name.title()

original_name = formatted_frnd_name('killari','naveen')
print(original_name)

def cars_old(car_1,car_2):
    car_order = (f"{car_1} and then {car_2}")
    return(car_order.title())
order_of_car = cars_old('bolero','XL-6')
print(order_of_car)

print("\n")

# PRACTISE ----->
# 1)The Cash Register
def get_total_bill(price,tax_rate):
    calculated_price = price + (price * tax_rate)
    return(calculated_price)

final_bill = get_total_bill(500,0.18)
print(final_bill)

print("\n")

# 2)Clean Nmae formatter
def format_full_name(first_name,last_name):
    new_formated_name = (f"{first_name.strip()} {last_name.strip()}")
    return(new_formated_name.title())
new_name = format_full_name("   virat ",'kOhLi')
print(f"Player registeted : {new_name}")
