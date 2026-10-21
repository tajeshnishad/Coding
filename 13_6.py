# function with a while loop 
def formatted_name(f_name,l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()
active = True
while active:
    print("\nPlease tell me your name OR write 'quit' to stop furter entery ")
    first_name = input("Tell me your 1st name : ")
    second_name = input("Tell me your second name : ")
    if first_name == 'quit':
        active = False
    else:
        format_name = formatted_name(f_name = first_name,l_name = second_name)
        print(format_name)
        break