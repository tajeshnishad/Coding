# 1
car='mahindra'
print("Is car== 'lexus'? I perdict False.")
print(car=='lexus')

print('\n')

car='RAM'
print("Is car = 'RAM'? I predict True.")
print(car=='RAM')

print('\n')

vip_guests = ['alice', 'brian', 'clara', 'david']
for guest in vip_guests:
    print(guest.title())
    if guest=='alice':
        print(f'{guest.title()}, gets a front row seat!')
    else:
        print(f"{guest.title()}, gets a standard seat!")
print("All VIP guests have. been seated ")

print('\n')

available_items = ['laptop', 'mouse', 'monitor', 'keyboard']
order_items = ['mouse', 'printer', 'monitor']
print("Ordered items are:")
for order_item in order_items:
    print('\n')
    print(order_item.title())
    if order_item in available_items:
        print(f"Adding {order_item.title()} in your list")
    else:
        print(f"{order_item} out of stock!")

print("Order processing completed!")

print("\n")

ages = [4, 15, 28, 70]
for age in ages:
    print(age)
    if 0<=age<5:
        print("Admission is free")
    elif 5<=age<18:
        print("Admission is $10")
    elif 18<=age<65:
        print("Admission is $20")
    else:
        print("Admission is $12 for seniors")

print("All ticket prices calculated")

print('\n')

current_users = ['Admin', 'John', 'Sarah', 'Alex', 'Mike']
new_users = ['sarah', 'CHRIS', 'mike', 'Emma']

