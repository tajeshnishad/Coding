# If Statement (Checking Inequality )

requesting_toppig='mushroom'
if requesting_toppig != 'anchovies':
    print('Hold the anchovoise!')

print('\n')

age = 18
if age != 20:
    print("candidate is under age ")

print('\n')

print(f'{age==18},Candidate Voating')

print('\n')

answer = 42
if answer != 7 :
    print("Answer is incorrect plz ,do it again")

print('\n')

girl_age=20
if girl_age<=18:
    print("Minor")
else:
    print("Major")

print('\n')

age_0=22
age_1=18
print(f'{age_0>=23 and age_1<=19},false means ineligible and true means eligible')
print(f'{age_0>=23 or age_1<=19},false means ineligible and true means eligible')
print(f'{age_0==22 and age_1==18}, Hi! how u both are doing ')
print(f'{age_0==22 or age_1==18}, Hi! how u both are doing ')

print('\n')

requested_topping=['mushroom','onions','pineapple']
print('mushroom' in requested_topping)

print('\n')

user_names=['sunny','tjesh','naveen']
if user_names=='akash':
    print("user name already taken , use different user name")
else:
    print("user name not taken you can use it")

print('\n')

banned_user=['kabir','ashish','avinash','mrinalini']
user='naveen'
if user not in banned_user:
    print(f'{user.title()}, you can do whatever you like')