# 1)Formatted City return
def city_country(city,country):
    print(f"\nCity : {city.title()}")
    print(f"Country : {country.title()}")
city_country("Santiago","Chile")
city_country("berlin","germany")
city_country("delhi","india")

print("\n")

# 2)Book Cataloger
def make_books(title,author,genere = 'Fiction'):
    info_bok = {'title' : title.title(),'author' : author.title(),'genere': genere.title()}
    print(info_bok)
make_books('1980','george orwell')
make_books('dune','frank herbert','sci-fi')
make_books('sapiens','yuval noah harari','non-fiction')

print("\n")

# 3)Music Album with Optional Parameter
def make_album(artist,title,songs = None):
    if songs:
        music_info ={'Artist name' : artist.title(),'Album name' : title.title(),'Songs' : songs}
    else:
        music_info ={'Artist name' : artist.title(),'Album name' : title.title()}
    return music_info

album = make_album('pink floyd','the wall')
print(album)
album = make_album('draft punk','discovery')
print(album)
album = make_album('adele',title= '30', songs= 12)
print(album)

print("\n")

# 4)voting age vrification
def can_vote(age):
    if age >= 18:
        print(f"Age {age}: Eligble to vote")
    else:
        print(f"Age {age}: Not eligible to vote")

can_vote(20)
can_vote(15)