# EXERCISE 2-9: Number Eight
# Prompt: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your 
# operations in print() calls to see the results. You should create four 
# lines that look like this: print(5+3)
print(5+3)      #8
print(9-1)      #8
print(4*2)      #8
print(16//2)    #8
print(16/2)     #8.0
"""Inspite of LINE 4 and LINE 5 being litte different becz
line 4 has ---> '//' which means it wil devide the number at the same time it will also GIVE CLEANER OUTPUT without any decimal and rounding it off and give INTEGER VALUE AS OUTPUT
but in 
line 5 has ---> '/' which means it will devide the number but it will GIVE OUTPUT IN FLOAT  """


# EXERCISE 2-10: Favorite Number
# Prompt: Use a variable to represent your favorite number. Then, 
# using that variable, create a message that reveals your favorite 
# number. Print that message.
fav_number=47
f_name='tajesh'
l_name='nishad'
full_name=f'{f_name} {l_name}'
print(f'Hello {full_name.title()}, your favourit number is {fav_number}')