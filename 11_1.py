# Adding new key-value pairs
aline_0={'color':'pink','points':20}
print(aline_0)

aline_0['x_position']=0
aline_0['y_position']=25
print(aline_0)

print('\n')

alien_1={}
alien_1['colour']='green'
alien_1['points']=15
alien_1['tran_mode']='fly'
print(alien_1)
print(f"Alien is now {alien_1['colour']}")
alien_1['colour']='black'
print(alien_1)
print(f"Alien is now {alien_1['colour']}")

print("\n")

alien_2={'x_position':0,'y_position':25,'speed':'slow'}    # NOTE : here value of 'speed ' = 'slow' 
alien_2['speed']='fast'                                    # NOTE : Updated value of 'speed' ='fast'
print(f"Original Position : {alien_2['x_position']}")
if alien_2['speed']=='slow':
    x_increament = 1
elif alien_2['speed']=='medium':
    x_increament = 2
else:
    x_increament=3
alien_2 ['x_position']=alien_2['x_position'] + x_increament
print(f"New position : {alien_2['x_position']}")
