# """ Assign a 'message' to a variable ,and then print that message """
a='message'
print(a)

# '''assign a message to a variable , and print that message. Then change the value of the variable to a new message'''
a='message'
print(a)
a='i m overwritting a message command'
print(a)



# EXERCISE 1: Personal Message
# Prompt: Use a variable to represent a person’s name, and print a message to 
# that person. Your message should be simple, such as, "Hello Eric, would you 
# like to learn some Python today?"
f_name='eric'
message=f'"Hello {f_name.title()},would you like to learn some Python today?"';
print(message);



# EXERCISE 2: Name Cases
# Prompt: Use a variable to represent a person’s name, and then print that 
# person’s name in lowercase, uppercase, and title case.
f_name='tajeSh'
l_name='NISHad'
full_name=f'{f_name} {l_name}'
print(full_name.lower());
print(full_name.upper());
print(full_name.title());



# EXERCISE 3: Famous Quote
# Prompt: Find a quote from a famous person you admire. Print the quote and the 
# name of its author. Your output should look something like the following, 
# including the quotation marks:
# Albert Einstein once said, "A person who never made a mistake never tried 
# anything new."
fav_person='Daya ram sahini'
message=f'{fav_person.title()} once said "A person should not teach about dharma to a hungry people, instead give him some food "'
print(message)



# EXERCISE 4: Famous Quote 2
# Prompt: Repeat Exercise 2-5, but this time, represent the famous person’s 
# name using a variable called famous_person. Then compose your message and 
# represent it with a new variable called message. Print your message.
famous_person='daya ram sahini'
message=f'{famous_person.title()} once said "A person should not teach about dharma to a hungry people, instead give him some food "'
print(message)



# EXERCISE 5: Stripping Names
# Prompt: Use a variable to represent a person’s name, and include some 
# whitespace characters at the beginning and end of the name. Make sure you use 
# each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print 
# the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
p_name=' kishan  '
l_name=' nishad'
full_name=f'{p_name.rstrip()} {l_name.lstrip()}'
print(full_name.rstrip())
print(full_name.lstrip())
print(full_name.strip())
# n_line=f'{full_name.title()}';
# print('\t',n_line())
# print('\n',n_line())
# print('\t\n',n_line())
print('\t kishan nishad \n');


# EXERCISE 6: File Extensions
# Prompt: Python has a removesuffix() method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename. Then use the 
# removesuffix() method to display the filename without the file extension, like 
# some file browsers do.
message='https://python_notes.txt'
print(message.removesuffix('.txt'))
print(message.removeprefix('https://'))
