# 1)people
people_0 = {'first_name' : 'vaibhav',
          'last_name' : 'nishad',
          'age' : '21',
          'city' : 'kanker'}
people_1 = {'first_name' : 'anshul',
          'last_name' : 'dalal',
          'age' : '24',
          'city' : 'haryana'}
people_2 = {'first_name' : 'minal',
          'last_name' : 'nishad',
          'age' : '22',
          'city' : 'raipur'}
peoples_l = [people_0,people_1,people_2]
for people_l in peoples_l:
    print("\n")
    for people,specs in people_l.items():
        print(f"{people.title()} : {specs.title()}")

print("\n")

# 2) Pets
pet_0 = {'dog_breed':'german sephard','owner_name':'minal'}
pet_1 = {'dog_breed':'golden retriver','owner_name':'anshul'}
pet_2 = {'dog_breed':'labrador retriver','owner_name':'kabir'}

pets = [pet_0,pet_1,pet_2]

for pet in pets:
    print("\n")
    for criteria,name in pet.items():
        print(f"{criteria.title()} : {name.title()}")

print("\n")

# 3)Favourite Places
favourite_places = {'sunny' : ['chitrookot','taj mahal','mysur palace'],
                    'kabir' : ['new york','manali','dargelling'],
                    'vaibhav' : ['danteshwari','bamleshwari','go karting']}

favourite_places['minu'] = ['wonderla','water park']

for name,placecs in favourite_places.items():
    print(f"\n{name.title()}'s favourite places to visit his are:")
    for place in placecs:
        print(f"{place.title()}")

print("\n")

# 4)Favourite Number
fav_number = {'naveen' : [15,11],
              'ansul' : [2,61],
              'ikku' : [17,21],
              }
fav_number['minu'] = [43,31]

for names_n,values_n in fav_number.items():
    print(f"\n{names_n.title()}'s favourite number are:")
    for values_x in values_n:
        print(f"\t{values_x}")

print("\n")

cities = {'raipur': {'fact': 'place of my hometown','country' : 'india' , 'population' : 15_00_000},
          'durg' : {'fact': 'place of my father hometown','country' : 'india' , 'population' : 16_00_000}, 
          'secunderabad' : {'fact' : 'place where i have my most wonderful memories in' ,'country' : 'india','population' : 1_10_00_000}
          }

cities['berlin'] = {'fact':'Capital city of germany','country':'germany','population' : 30_00_000}

for city,informations in cities.items():
    print(f"\n{city.title()} more detailed informations are:")
    for key,information in informations.items():
        if information in ['india' and 'germany']:
            print(f"{key.title()} : {information.upper()}")
        else:
            print(f"{key.title()} : {information}")

print("\n")

# 5) Extentions
users = {
    'aienstien' : {'f_name':'albert','l_name':'einstien','location':'princeton'},
    'mcurie' : {'f_name':'marie','l_name':'curie','location':'paris'},
    'abhatta' : {}
}
users['aienstien']['about'] = 'he was a greatest scientest of all time.'    #NOTE: Keep in Mind
users['abhatta']['f_name'] = 'arya'
users['abhatta']['l_name'] = 'bhatta'
users['abhatta']['location'] = 'india'
users['abhatta']['about'] = 'gretest mathematican of all time.'
print(users['aienstien']['location'])                                        #NOTE: Keep in Mind
print("\n")
print(users)
for username,user_datas in users.items():
    print(f"\nAbout {username.title()}")
    for key,user_data in user_datas.items():
        print(f"{key} : {user_data}")