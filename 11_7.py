aliens=[]

for alien_numbers in range(30):
    alien_d={'color':'green','points':'12','speed':'slow'}
    aliens.append(alien_d)

for alien_y in aliens[:3]:
    if alien_y['color'] == 'green':
        alien_y['color'] = 'yellow'
        alien_y['points'] = 20
        alien_y['speed'] = 'medium'

for alien_f in aliens[:5]:
    print(alien_f)