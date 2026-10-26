# Challenge 1: Smart Home Device Registrar
def register_device(room,device_type,**extra_info):
    extra_info['Room'] = room
    extra_info['Device type'] = device_type
    return extra_info
device = register_device('Living Room', 'Smart Bulb', brightness=85, status='on')
print(device)

print("\n")

# Challenge 2: Book Title Formatter
def format_book(title,author,year = None):
    if year == None:
        print(f"{title.title()} by {author.title()}")
    else:
        print(f"{title.title()} by {author.title()} ({year})")

format_book('the hobbit', 'j.r.r. tolkien', year=1937)
format_book('1984', 'george orwell')

print("\n")

# Challenge 3: Grocery Bag Packer
def pack_groceries(unpacked,grocrey_bag):
    list(unpacked)
    list(grocrey_bag)
    while unpacked:
        current_package = unpacked.pop()
        grocrey_bag.append(current_package)
        print(f"Packing: {current_package}")

cart = ['Apples', 'Milk', 'Bread']
bag = []

pack_groceries(cart, bag)
print(f"Bag contents: {bag}")
print(f"Cart left: {cart}")

print("\n")

# Challenge 4: Pizza Order Summary
def make_pizza(size,*pizza_info):
    pizza_info = list(pizza_info)
    print(f"Making a {size}-inch pizza with the following toppings:")
    for pizza in pizza_info:
        print(f"- {pizza}")

make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')

print('\n')

# Challenge 5: Inventory Restock Checker

def check_stock(stocks,threshold = 5):
    restock_lst = []
    for key,value in stocks.items():
        if value <= threshold :
            restock_lst.append(key)
    return restock_lst

stock = {'notebooks': 12, 'pens': 3, 'erasers': 1, 'markers': 8}
restock_list = check_stock(stock, threshold=4)
print(f"Need to restock: {restock_list}")

print("\n")

# Challenge 6: City Description
def describe_city(city,country = "India"):
    print(f"{city.title()} is in {country}")

describe_city('Mumbai')
describe_city('Raipur')
describe_city('Tokyo', 'Japan')

print("\n")

# Challenge 7: Safe Message Archiver
def archive_messages(inboxes):
    for inbox_ in inboxes:
        print(f"Archived: {inbox_}")

inbox = ['Hello', 'Meeting at 5', 'Your OTP is 1234']
archive_messages(inbox[:])
print(f"Original inbox: {inbox}")