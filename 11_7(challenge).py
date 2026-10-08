# 1) The armour upgrade
soldiers=[]

for soldier in range(6):
    soldier_d={'rank':'recruit','armour':'50','status':'active'}
    soldiers.append(soldier_d)

for soldiers_3 in soldiers[:3]:
    if soldiers_3['rank'] == 'recruit':
        soldiers_3['rank'] = 'veteran'
        soldiers_3['armour'] = '100'

for soldiers_l in soldiers:
    print(soldiers_l)
print("...done...")

# 2)The Fleet INterceper
fleet = [
    {'ship_id': 'Falcon-1', 'fuel': 85, 'cleared_for_flight': False},
    {'ship_id': 'Apollo-2', 'fuel': 40, 'cleared_for_flight': False},
    {'ship_id': 'Nova-3', 'fuel': 92, 'cleared_for_flight': False},
    {'ship_id': 'Viper-4', 'fuel': 20, 'cleared_for_flight': False},
]

for fleet_d in fleet:
    if fleet_d['fuel'] >= 50:
        fleet_d['cleared_for_flight'] = 'True'
        print(fleet_d)

for cleared_for_flight in fleet:
    if cleared_for_flight['cleared_for_flight'] == 'True':
        print(f"Ship {cleared_for_flight['ship_id']} is cleared with {cleared_for_flight['fuel']}% fuel.")
    else:
        print(f"Ship {cleared_for_flight['ship_id']} is Not-cleared with {cleared_for_flight['fuel']}% fuel.")

# 3) Loot tracker
chests = [
    {'chest_id': 1, 'gold': 50, 'has_gem': True},
    {'chest_id': 2, 'gold': 20, 'has_gem': False},
    {'chest_id': 3, 'gold': 100, 'has_gem': True},
    {'chest_id': 4, 'gold': 35, 'has_gem': False},
    {'chest_id': 5, 'gold': 80, 'has_gem': True},
]

total_gold=0
gem_count=0
for chest in chests:
    total_gold += chest['gold']
    if chest['has_gem'] == True:
        gem_count += 1
print(total_gold)
print(gem_count)
 