# Returning a Dictionary
def formatted_name(f_name,l_name):
    full_name = {f"first name : {f_name}, second name : {l_name}"}
    return full_name

final_name = formatted_name('Minal','Nishad')
print(final_name)

print("\n")

def build_person(first_name,last_name,age = None):
    person = (f"first : {first_name}, last : {last_name} ")
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] =  age
    return person
mucisian = build_person('jimi','hendrix',age = 23)
print(mucisian)

 