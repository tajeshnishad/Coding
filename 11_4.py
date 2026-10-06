# Looping through all Keys in Dictionary
fav_languages={'naveen':'pharma','sunny':'python','anshul':'rust'}
friends=['naveen','anshul']
for names in fav_languages.keys():
    print(f"Hi {names.title()}")

    if names in friends:
        language=fav_languages[names]
        print(f"\t{names.title()} fav. language is {language.title()}")

print("\n")

favo_languages={'naveen':'pharma','sunny':'python','anshul':'rust'}
if 'kabir' not in favo_languages.keys():
    print(f"Kabir is yet to poll!")

print("\n")

favou_languages={'naveen':'pharma','sunny':'python','anshul':'rust'}
for name in sorted(favou_languages.keys()):
    print(f"{name.title()}, thanks for taking the poll")
print(favou_languages)

print("\n")

favour_languages={'naveen':'pharma','sunny':'python','anshul':'rust'}
for languages in sorted(favou_languages.values()):
    print(f"Peoples fav. is {languages.title()}")

print("\n")

favouri_languages={'naveen':'pharma','sunny':'python','anshul':'rust','kabir':'python'}
print("Following languages are the lanuges people's opted for:")
for lang in set(favouri_languages.values()):
    print(lang.title())