# List in a Dictionaries
pizza={'crust':'thick',
       'toppings':['mushroom','extra cheese']}
print(f"you ordered a {pizza['crust']}-crust pizza"
      " with the following toppings :")
for topping in pizza['toppings']:
    print(f'\t{topping}')

print("\n")

favourite_languages={'naveen':['python','rust'],
                     'anshul':['c'],
                     'kabir':['rust','go'],
                     'sunny':['python','XXAMP']}
langugees = favourite_languages.values()
if len(langugees) >= 2:
    for names,langugees in favourite_languages.items():
        print(f"{names.title()}'s favourite languages are:")
        for language in langugees:
            print(language.title())
