fav_languages = {'anshul' : ['rust','python','c++'],
                 'naveen' : ['b.pharma','python'],
                 'kabir' : ['c++','ios','rust']}
fav_lang = []
for names,languages in fav_languages.items():
    for language in languages:
        fav_lang.append(language)
print(set(fav_lang))