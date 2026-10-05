# Dictionaries

aline_0={'color':'green','points':5}
print(aline_0['color'])
print(aline_0['points'])

print("\n")

aline_1={'color':'blue','points':10}
print(aline_1['points'])
print(aline_1['color'])

print("\n")

aline_2={'color':'white'}
print(aline_2['color'])

print("\n")

alien_3={'color':'green','points':5}
if alien_3['color']=='green':
    new_points=alien_3['points']
    print(f"Player has earned {new_points} points!")