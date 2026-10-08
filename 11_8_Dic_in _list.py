alines=[]
for aline in range(10):
    aline = {'color':'green','speed':'slow','points':5}
    alines.append(aline)

for aline_1 in alines[:5]:
    if aline_1['color'] == 'green':
        aline_1['color'] = 'yellow'
        aline_1['speed'] = 'medium'
        aline_1['points'] = 10

for alien_2 in alines[:2]:
    if alien_2['color'] == 'yellow':
        alien_2['color'] = 'red'
        alien_2['speed'] = 'fast'
        alien_2['points'] = 15

for alien_3 in alines:
    print(alien_3)