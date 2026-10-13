# Using Break statement
prompt = '\nPlease enter the name of a city you have visited'
prompt += '\nEnter "quit" when you are finished : '
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I have visited {city.title()} city. ")

print("\n")

