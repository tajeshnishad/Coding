# # 1) Deli
sandwich_orders = ['Bombay Masala Grilled Sandwich','Falafel Pita','Caprese','Lobster Roll']
finished_orders = []

print(f"Your requested Sandwich's are : ")
for sandwi in sandwich_orders:
    print(sandwi)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_orders.append(sandwich)
    print(f"Finished your {sandwich.title()} sandwich. Preparing for next one!")

print(f"---Request Compleated---")
print("Finishing your order one-by-one plz wait!")
for orders in finished_orders:
    print(orders.title())

# 1_1) Taking user input in same 
sandwich_orders = '\nEnter the sandwich you would like to eat'
sandwich_orders += '\nEnter "done" to stop adding more items in it : '
sandwich_request = []
finished_sandwiches = []
activity = True
while activity:
    sandwich = input(sandwich_orders)
    if sandwich == 'done':
        activity = False
    else:
        sandwich_request.append(sandwich.title())

print(f"\nYour requested sandwiches are : ")
for sannd in sandwich_request:
    print(sannd)
print("\n")
while sandwich_request:
    finishing = sandwich_request.pop()
    finished_sandwiches.append(finishing)
    print(f"Finished making your {finishing} sandwich")

print(f"\nYour order's completed")
for finished in finished_sandwiches:
    print(finished)
print("----Thanku---- VISIT AGAIN!!!")