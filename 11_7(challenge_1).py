# 1)The Inventory Restock(Threshhold Check and Increment)
warehouse = [
    {'item': 'mouse', 'stock': 14, 'needs_restock': False},
    {'item': 'keyboard', 'stock': 4, 'needs_restock': False},
    {'item': 'monitor', 'stock': 2, 'needs_restock': False},
    {'item': 'headset', 'stock': 20, 'needs_restock': False},
    {'item': 'webcam', 'stock': 5, 'needs_restock': False},
]     #LIST

for warehouse_1 in warehouse:
    if warehouse_1['stock'] <= 6:
        warehouse_1['needs_restock'] = True
        warehouse_1['stock'] += 10

for warehouse_2 in warehouse:
    if warehouse_2['needs_restock'] == True:
        print(f"{warehouse_2['item']} now has {warehouse_2['stock']} in stock after restock.")

print("\n")

# 2) The Student Scored(Grade Evaluation and Avegage)

students = [
    {'name': 'rohit', 'score': 78, 'passed': False},
    {'name': 'simran', 'score': 42, 'passed': False},
    {'name': 'aman', 'score': 91, 'passed': False},
    {'name': 'priya', 'score': 33, 'passed': False},
    {'name': 'kunal', 'score': 65, 'passed': False},
]
total_score = 0
passed_count = 0

for students_1 in students:
    total_score += students_1['score']
    if students_1['score'] >= 50 :
        students_1['passed'] = True
        passed_count += 1

avg_sore = 0
avg_sore = total_score/len(students)
print(f'Average score of the class is {avg_sore}')
print(f"Number of students passed are {passed_count}")

print("\n")

# 3) The Sensore Alarm(Locating a specific Target & Flagging)
servers = [
    {'server_id': 'srv-1', 'temp': 45, 'status': 'normal'},
    {'server_id': 'srv-2', 'temp': 82, 'status': 'normal'},
    {'server_id': 'srv-3', 'temp': 55, 'status': 'normal'},
    {'server_id': 'srv-4', 'temp': 90, 'status': 'normal'},
]

for server_1 in servers:
    if server_1['temp'] > 75:
        server_1['status'] = 'CRITICAL'
    else:
        server_1['status'] = 'normal'

for server_2 in servers:
    if server_2['status'] == 'CRITICAL':
        print(f"WARNING: Server {server_2['server_id']} is running hot at {server_2['temp']}")
    else:
        print(f"Server {server_2['server_id']} is operating normally.")