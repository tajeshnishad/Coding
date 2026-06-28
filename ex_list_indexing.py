# EXERCISE 3-1: Names
# Prompt: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.
names=['naveen','lucky','aryan','bhumi']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())



# EXERCISE 3-2: Greetings
# Prompt: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each 
# message should be the same, but each message should be personalized with
print(f'{names[0].title()},is my best friend ')
print(f'{names[1].title()},is my APSB school friend ')
print(f'{names[2].title()},is my Prahar friend ')
print(f'{names[3].title()},is my Prahar Female friend ')



# EXERCISE 3-3: Your Own List
# Prompt: Think of your favorite mode of transportation, such as a motorcycle 
# or a car, and make a list that stores several examples. Use your list to 
# print a series of statements about these items, such as "I would like to own a Honda motorcycle."
bikes_cars=['BMW(M3)','BMW(1000RRm)','triumph(rocket3_RGT)','Defender']
print(f'{bikes_cars[0].title()},is my dream car')
print(f'{bikes_cars[1].title()},is my favrout moto GP bike ')
print(f'{bikes_cars[2].title()},is the only bike in bike industery with 2500CC Engine ')
print(f'{bikes_cars[-1].title()},is my dream car and i will purchase it for sure ')