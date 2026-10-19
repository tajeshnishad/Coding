# Making an Argument optional
def get_formatted_name(f_name,l_name,m_name=''):
    full_name = (f"{f_name} {m_name} {l_name}")
    return full_name.title()

final_ful_name = get_formatted_name('kilari','kumar',m_name='naveen')
print(final_ful_name)

fnl_name = get_formatted_name('anshul','dalal')
print(fnl_name)

# OR 
print("\n")

def get_name(f_name,l_name,m_name=''):
    if m_name:
        ful_name = f"{f_name} {m_name} {l_name}"
    else:
        ful_name = f"{f_name} {l_name}"
    return ful_name.title()

new_full_name = get_formatted_name(f_name='kilari',m_name='naveen',l_name='kumar')
print(new_full_name)

new_full_name = get_formatted_name('TaJesh','Nishad')
print((new_full_name))