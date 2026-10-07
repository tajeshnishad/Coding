
# list for storing aliens
aliens=[]

# Storing 30 green aliens
for alien_number in range(30):
    alien_l={'color':'green','points':'15','speed':'slow'}
    print(f"{alien_l}")
    aliens.append(alien_l)

print("\n")

# showing the first 5 aliens
for alien_p in aliens[:5]:
    print(alien_p)
print("...")

# showing how many aliens have been created so far 
print(f"Number of aliens created are {aliens.__len__()}")