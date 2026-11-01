# Problem 1: Normalized Contact Card 
def create_contact(first_name,last_name,phone=None,**extra_details):
    for key,value in extra_details.items():
        if isinstance(value, str):
            extra_details[key] = value.strip()
    extra_details['name'] = f"{first_name.strip().title()} {last_name.strip().title()}"
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

print("\n")

# Problem 3: Sensor Outlier Filter 
def filter_readings(readings,min_value=10,max_value=100):
    clean_data = []
    for value in readings:
        if min_value <= value <= max_value:
            clean_data.append(value)
    return clean_data

raw_data = [5, 12, 85, 102, 50, 9, 100]
clean_data = filter_readings(raw_data, min_value=10, max_value=90)

print("Cleaned:", clean_data)
print("Original:", raw_data)

print("\n")

# Problem 4: Dynamic Query String Builder 
def build_query_url(base_url,*path_segments,**parameters):
    ulrs = [base_url]
    for path_segment in path_segments:
        ulrs.append(f"/{path_segment}")
    if parameters != None:
            ulrs.append("?")
            for key,values in parameters.items():
                ulrs.append(f"{key}={values}&")
    current_url = ''
    for ulr in ulrs:
        current_url += ulr

    return current_url
    

url1 = build_query_url("https://api.site.com", "v1", "users", role="admin", active="true")
url2 = build_query_url("https://api.site.com", "status")
url3 = build_query_url("https://api.site.com/", "v2", "reports/", sort="asc")

print(url1)
print(url2)
print(url3)

print("\n")

# Problem 5: Ticket Priority Dispatcher
def dispatch_queue(unhandeled_tickets,processed_tickets,priority_flag='URGENT'):
    while unhandeled_tickets:
        current_ticket = unhandeled_tickets.pop(0)
        if priority_flag in current_ticket:
            processed_tickets.append(f"[EXPEDITE] {current_ticket}")
        else:
            processed_tickets.append(f"{current_ticket}")

incoming = ['Login issue', 'Server crash (URGENT)', 'Password reset', 'Payment failure (URGENT)']
completed = []
dispatch_queue(incoming, completed)

print("Incoming remaining:", incoming)
print("Completed queue:", completed)

print("\n")

# Problem 6: Word Frequency Analyzer 
def word_tally(sentence):
    
    clean_sentence = sentence.lower()
    for char in [".", ",", "!"]:
        clean_sentence = clean_sentence.replace(char, "")
 
    words = clean_sentence.split()

    tally = {}
    for word in words:
        if word in tally:
            tally[word] += 1
        else:
            tally[word] = 1

    return tally


# Test Case
sample = "Python is great, and Python is simple and fun!"
result = word_tally(sample)
print(result)