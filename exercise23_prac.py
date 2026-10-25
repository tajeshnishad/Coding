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
