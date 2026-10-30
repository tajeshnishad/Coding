# Problem 1: Normalized Contact Card 
def create_contact(first_name,last_name,phone=None,**extra_details):
    extra_details['name'] = f"{first_name.title()} {last_name.title()}"
    if phone is not None:
        extra_details['phone'] = phone
        info = extra_details
        return info
    else:
        info = extra_details
        return info

c1 = create_contact("  arjun ", "sharma  ", phone="9876543210", city="  Raipur ", verified=True)
c2 = create_contact("priya", "verma")

print(c1)
print(c2)

print("\n")

# Problem 2: Inventory Depletion Engine 
fulfilled = []
failed = []
updated_stock = {}
def process_orders(orders,available_stock):
    for keys,values in available_stock.items():
        for order in orders:
            if order[0] == keys:
                if available_stock[keys] >= order[1]:
                    fulfilled.append(keys)
                    value = available_stock[keys] - order[1]
                    updated_stock[order[0]]=value
        if order[1]>available_stock[keys]:
                failed.append(keys)

    report = report = f"""Fullfilled: {fulfilled}
            Failed: {failed}"""    
    return report

current_stock = {'pen': 10, 'notebook': 3, 'eraser': 5}
order_list = [('pen', 4), ('notebook', 5), ('ruler', 1), ('eraser', 5)]

report = process_orders(order_list,current_stock)
print("Report:", report)
print("Updated Stock:", updated_stock)