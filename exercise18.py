# 1) Glossary 2:
glossaries={'{}':'inside it is dictionary','[]':'inside it is list','()':'inside it is tuple'}
for glossary in glossaries.items():
    print(glossary)
glossaries['set()']='it take unique items only'
glossaries['keys()']='it takes all keys of a dictionary'
glossaries['values()']='it takes all values of a dictionary'
glossaries['soted()']='it takes all keys of a dictionary short i alphabetical order'
for key,value in glossaries.items():
    print(key)
    print(f"\t{value}")

maj_rivers={'india':'ganga','egypt':'nile','china':'tsangpoo'}
for country,river in maj_rivers.items():
    print(f"{country.title()} major flowing river is {river.title()}")
print("Finished")

print("\n")

# 3) favourite language
fav_language={'naveen':'pharma','anshul':'rust','kabir':'C++'}
polling_person=['naveen','ishita','sunny','ikku','kabir']
for poll_person in polling_person:
    if poll_person in fav_language.keys():
        print(f"{poll_person.title()} has already voted!")
    else:
        print(f"{poll_person.title()} is invited o take the vote!")