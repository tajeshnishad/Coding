# Dictionaries inside Dictionaries
users = {'Tnishad' : 
         {'first_name' : 'Tajesh',
          'last_name' : 'nishad',
          'location' : 'chhattisgarh'},
          'Vnishad' :
          {'first_name' : 'vaibhav',
           'last_name' : 'nishad',
           'location' : 'chhattisgarh'
           }
          }
for keys,values in users.items():
    print(f"Username : {keys}")
    for key,value in values.items():
        print(f"{key.title()} : {value.title()}")
    print("\n")