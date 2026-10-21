# 1)City Names
def city_country(city,country):
    print(f"{city.title()}, {country.title()}")
city_country('santiago','chile')
city_country('jaipur','india')
city_country('berlin','germany')
city_country('moscow','russia')

print("\n")

# 2) Make album
def make_album(artist_name,artist_title,num_songs = None):
    album = f"{artist_name.title()} : {artist_title} , Number of songs : {num_songs}"
    return album
album = make_album('adle','Rolling in the deep')
print(album)
album = make_album('ed sheeran','÷(DIVIDE)',23)
print(album)
album = make_album('arjit singh','Tum hi ho',234)
print(album)

print("\n")

# 3)User Album 
def make_albums(art_name,art_title,art_songs = None):
    albums = f"Artit name : {art_name.title()}, Title name : {art_title.title()}, Number of Songs : {art_songs} "
    return albums

flag = True
while flag:
    a_name = input("\nTell me artist name OR to stop press 'q': ")
    if a_name == 'q':
        flag = False
    a_title = input("Tell me title name : ")
    if a_title == 'q':
        flag = False
    a_total_songs = input("Total Number of songs : ")
    if a_total_songs == 'q':
        flag = False
    final_album = make_albums(art_name = a_name,art_title = a_title,art_songs = a_total_songs)
    if a_total_songs == '':
        final_album = make_albums(a_name,a_title)
        print(final_album)
    else:
        final_album = make_albums(a_name,a_title,a_total_songs)
        print(final_album)