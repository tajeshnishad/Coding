'''STRINGS'''
a='tajesh nishad'                                     
print(a.title());                                       '''function ----> title()[every word given as a input , its first letter will be capital]'''

print(a.upper());                                       '''function ----> upper()[it will turn all letters of a word given by user in CAPITALS(uppercase)]'''

print(a.lower());                                        '''function ----> lower()[it will turn all letters of a word given by user in LOWERCASE(small letters)]'''


# using variables in string
f_name='tajesh';
l_name='nishad';
full_name=f'{f_name} {l_name}';
print(full_name.title());

message=f'Hello ,{f_name} {l_name} its good to see you again !';                          '''OUTPUT ----> Hello ,Tajesh Nishad Its Good To See You Again !'''
print(message.title());

mesg=f'hello ,{full_name.title()}'
print(mesg);                                                                              '''output----> hello ,Tajesh Nishad'''

print(mesg.title());                                                                       '''output---->Hello ,Tajesh Nishad'''