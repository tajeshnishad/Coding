def formated_name(unauthorised_person,authorised_person):
     while unauthorised_person:
        current_person = unauthorised_person.pop()
        print(current_person)
        authorised_person.append(current_person.title())
def auth_person(authorised_person):
     for person in authorised_person:
          print(person)

unrecognised_person = ['sony','kabir','JBL','anshul']
recgnised_person = []

print("Unauthorised persons are : ")
formated_name(unrecognised_person,recgnised_person)
print("\n")
print(f"Authorised persons are  : ")
auth_person(recgnised_person)