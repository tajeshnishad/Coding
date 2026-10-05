# Removing Key value pairs
alien_0={'color':'white','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

# Dictionaries of similar objects
favoutrite_languages={
    'kabir':'C++',
    "avinash":'C',
    "shoumik":"python",
    "tajesh":'python',
}
print(favoutrite_languages)
print(favoutrite_languages['kabir'])

print("\n")

alien_1={'color':'titanium','speed':'slow'}
# print(alien_1['points'])
points__value=alien_1.get("points",'No value assigned.')
print(points__value)