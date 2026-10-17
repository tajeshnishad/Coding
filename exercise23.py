# 1)T-Shirt
def make_shirt(shirt_size,shirt_text):
    print(f"\nSize of the shirt will be : {shirt_size} \nText written on it would be : {shirt_text} ")
make_shirt(23,'NEVER GIVE UP')
make_shirt(shirt_size='L',shirt_text='Make yourself stronger than your excues')

print("\n")

# 2) Large Shirts
def make_shirt(size_shirt = 'Large',message = 'I Love Python'):
    print(f"\nsize : {size_shirt}, Message. : {message}")

make_shirt()
make_shirt(size_shirt='Medium')
make_shirt(size_shirt='Small',message= 'Code never sleeps' )

print("\n")

# 3)Cities
def describe_city(city_name,city_country='india'):
    print(f"\n{city_name.title()} is in {city_country.title()}")
describe_city('rejkjavik','iceland')
describe_city(city_name='raipur')
describe_city('punjab','pakistan')