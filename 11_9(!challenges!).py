# 1)The space probe Telemetry (Multi Conditions State Update)

space_probes = [
    {'probe_name': 'Voyager', 'battery': 45, 'signal_strength': 'weak', 'in_safe_mode': False},
    {'probe_name': 'Curiosity', 'battery': 80, 'signal_strength': 'strong', 'in_safe_mode': False},
    {'probe_name': 'Pioneer', 'battery': 20, 'signal_strength': 'none', 'in_safe_mode': False},
    {'probe_name': 'Perseverance', 'battery': 95, 'signal_strength': 'moderate', 'in_safe_mode': False},
]

for spacce_probe in space_probes:
    if spacce_probe['battery'] <= 50 or spacce_probe['signal_strength'] == 'none':
        spacce_probe['in_safe_mode'] = True

for space_probe in space_probes:
    probe_name = space_probe['probe_name']
    if space_probe['in_safe_mode'] == True:
        print(f"Probe {probe_name.title()} is entering SAFE MODE due to critical telemetry.")
    else:
        print(f"Probe {probe_name.title()} is active and transmitting normally.")

print("\n")

# 2) The Cyber Defence Port Filter(Threshold Flags and Counter)

network_ports = [
    {'port': 22, 'traffic_mb': 450, 'is_flagged': False},
    {'port': 80, 'traffic_mb': 1200, 'is_flagged': False},
    {'port': 443, 'traffic_mb': 3500, 'is_flagged': False},
    {'port': 8080, 'traffic_mb': 1800, 'is_flagged': False},
    {'port': 21, 'traffic_mb': 90, 'is_flagged': False},
]

flagged_count=0

for network_port in network_ports:
    if network_port['traffic_mb'] > 1000:
        network_port['is_flagged'] = True 
        flagged_count += 1

print(f"Total suspicous ports flagged: <{flagged_count}>")

for network_port_1 in network_ports:
    if network_port_1['is_flagged'] == True:
        print(f"High traffic detected on port {network_port_1['port']} ({network_port_1['traffic_mb']}). ")

print("\n")

# 3)Train Revervation Surgee (Dynamic Price Adjustment)

train_passengers = [
    {'seat': 'B1', 'coach_type': 'sleeper', 'base_fare': 450, 'final_fare': 450},
    {'seat': 'A1', 'coach_type': 'ac_tier_2', 'base_fare': 1200, 'final_fare': 1200},
    {'seat': 'B4', 'coach_type': 'sleeper', 'base_fare': 450, 'final_fare': 450},
    {'seat': 'H1', 'coach_type': 'ac_tier_1', 'base_fare': 2100, 'final_fare': 2100},
]

for train_passenger in train_passengers:
    if train_passenger['coach_type'] == 'ac_tier_1':
        train_passenger['final_fare'] += 300
    if train_passenger['coach_type'] == 'ac_tier_2':
        train_passenger['final_fare'] += 150
    if train_passenger['coach_type'] == 'sleeper':
        train_passenger['final_fare'] = train_passenger['base_fare']

total_revenue = 0

for total_money in train_passengers:
    total_revenue += total_money['final_fare']

for updated_data in train_passengers:
    print(f"Seat {updated_data['seat']} ({updated_data['coach_type']}): Final Fare Rs{updated_data['final_fare']}")

print(f"Total tranin booking revenue : Rs<{total_revenue}>")


print("\n")


# 4) the University Course Registerar(Addding and Removing via list Operations)

department_courses = {
    'computer_science': ['algorithms', 'operating_systems', 'computer_networks'],
    'electronics': ['signals_and_systems', 'microprocessors'],
    'mechanical': ['thermodynamics', 'fluid_mechanics', 'machine_design'],
}
department_courses['computer_science'].append('compiler_design')
department_courses['electronics'].append('vlsi_design')

for courses,subjects in department_courses.items():
    if courses == 'computer_science':
        for subject in subjects:
            if subject == 'computer_networks':
                print(f"{subject.title()} is active in CS curriculum")

print(f"Mechinacal Department offers {len(department_courses['mechanical'])} core courses")

print("\n")

# 6) Drone waypoint Flight Path(Nested Loops and Coordinated)
drone_missions = {
    'alpha_survey': ['Point-A', 'Point-B', 'Base-1'],
    'bravo_patrol': ['Sector-4', 'Sector-5', 'Base-2', 'Perimeter-East'],
    'charlie_cargo': ['Depot-North', 'Dropzone-South'],
}

for types,surveys in drone_missions.items():
        print(f"\nMission {types} has {len(surveys)} assigned waypoints:")
        for survey in surveys:
            print(f"{survey.title()}")

print("\n")

# 5)Daily Running Distance Log(Data Analysis on Inner Lists)
weekly_runs_km = {
    'week_1': [5.2, 6.0, 5.0, 7.5],
    'week_2': [6.5, 7.0, 8.0, 6.0],
    'week_3': [4.0, 3.5, 5.0],
}
avg_distance = 0
for weeks,km_runs in weekly_runs_km.items():
    total_distance = sum(km_runs)
    avg_distance = total_distance/len(km_runs)
    if total_distance >= 25.0:
        print(f"{weeks.title()}: Outstanding training! Total distance: <{total_distance:.2f}>km (Avg: <{avg_distance:.2f}>km/run)")
    else:
        print(f"{weeks.title()}: Training target Pending! Total distance: <{total_distance:.2f}>km (Avg: <{avg_distance:.2f}>km/run)")

