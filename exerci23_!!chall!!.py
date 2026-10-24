# Challenge 1: The Magician Names
magician_names = ['harry houdini', 'david copperfield', 'dynamo']
def show_magicians(names):
    print(f"Name of all the magicians are : ")
    for name in names:
        print(name.title())
show_magicians(magician_names)

print("\n")

# Challenge 2: Sandwich Order Summary
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items: ")
    for item in items:
        print(item.title())
make_sandwich('cheese')   
make_sandwich('turkey', 'lettuce', 'tomato')   
make_sandwich('roast beef', 'cheddar', 'mayo', 'pickles')   

print("\n")

# Challenge 3: In-Place Fuel Efficiency Recalibration 
# def apply_mileage_tuning(reading, boost_percentage):

print("\n")

# Challenge 4: Parcel Courier Dispatch
def ship_package(reciepent, *contents,  delivery_type='Standard'):
    print(f"\nShipping to {reciepent.title()} via {delivery_type.title()} delivery:")
    for content in contents:
        print(f"- {content.title()}")

ship_package('arnav','notebook','pen',delivery_type='')
ship_package('pooja','laptop','Charger','mouse',delivery_type='express',)

print("\n")

# Challenge 5: Audit Log Sanitizer 
raw_users = ['raj', 'kiran', 'vikram']
sanitized = []
def mask_usernames(names_list):
    for names in names_list:
        current_user = f"USER_{names.upper()}"
        sanitized.append(current_user)
    print(f"Raw usera unchanged: {raw_users}")
    print(f"Sanitized list: {sanitized}")

mask_usernames(raw_users)

print("\n")

# Challenge 6: Task Queue Migrator 
pending = ['Setup DB', 'Write Tests', 'Deploy API']
finished = []
def process_queue(pending_tasks, finished_tasks):
    while pending_tasks:
        current_task = pending_tasks.pop(0)
        finished_tasks.append(current_task)
        print(f"Executing: {current_task}")

def summmerize_tasks(finished_tasks):
    print(f"Ttal finished tasks ({len(finished_tasks)}):")
    for finished_task in finished_tasks:
        print(f"- {finished_task.title()}")

process_queue(pending,finished)
print("\n")
summmerize_tasks(finished)
print(f"Pending list is now: {pending}")

print("\n")

# Challenge 7: Candidate Shortlist Filter
applicants = [
    {'name': 'Arjun', 'skill': 'Python'},
    {'name': 'Riya', 'skill': 'Java'},
    {'name': 'Karan', 'skill': 'Python'},
    {'name': 'Neha', 'skill': 'C++'}
]
target_skills = 'Python'
def shortlisted_candidates(applications, target_skill):
    selected = []
    for applicant in applications:
        if applicant['skill'] == target_skill:
            selected.append(applicant['name'].title())
    print(f"Shortlisted for Python: {selected}")
        
shortlisted_candidates(applicants,target_skills)

print("\n")

# Challenge 8: Server Cluster Configuration
def generate_server_config(server_name, ip_address, *flag, port=8080):
    server_config = f"{server_name}@{ip_address}.{port}"
    config = {
        'host':{server_config},
        'active_flag':list(flag),
        'flg_count':len(flag)
             }
    return config

configuration = generate_server_config('Alpha', '192.168.1.1', 'ssl', 'monitoring', 'auto_scale', port=443)
print(configuration)