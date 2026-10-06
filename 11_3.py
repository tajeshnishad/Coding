# using loops inside dictionary 
user={'username':'naveengalaxy','first_name':'naveen','last_name':'kilari'}
print(user['username'])
for key,value in user.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

print("\n")

alien={'name':'jadoo','color':'blue','type':'land','energy':'sun'}
for key,value in alien.items():
    print(f"\nkey : {key} ")
    print(f"value : {value}")

    print("\n")

fav_languge={'naveen':'pharma','sunny':'python','anshul':'linux'}
for person,language in fav_languge.items():
    print(f"\nperson : {person.title()}")
    print(f"language : {language.title()}")

print("\n")

favo_language={'naveen':'pharma','sunny':'python','anshul':'rust'}
for names in favo_language.keys():       # will pull only key's from dictionary
    print(f"Polled peoples is {names.title()}")
for language in favo_language.values():  # will pull only value's from dictionary
    print(f"\nFav. launguage is {language.title()}")