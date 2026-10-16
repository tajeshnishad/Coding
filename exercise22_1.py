sandwich_prompt = '\nEnter the sandwich you would like to have'
sandwich_prompt += '\nEnter "done" to stop giving the order : '
sandwich_orders = []
finished_orders = []
active = True
while active:
    order = input(sandwich_prompt)
    order = order.lower()
    if order == 'done':
        active = False
    elif order == 'paneer tikka':
        print("\nALERT! Paneer is not available (OUT OF STOCK)")
        pending = input(f"\nDo you want to give more orders beside's {order} (yes/no): ")
        if pending == 'yes':
            continue
        else :
            print()
            active = False
    else:
        sandwich_orders.append(order.title())

while sandwich_orders:
    order__ =sandwich_orders.pop()
    finished_orders.append(order__)
    print(f"\nFinished preparing your {order__}")

print(f"\nAll your compleated sandwiches are")
for finished in finished_orders:
    print(finished)