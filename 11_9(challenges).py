# 1) The Dev Stack Directory
developer_skills = {
    'alice': ['python', 'sql', 'docker'],
    'bob': ['c++', 'unreal_engine'],
    'charlie': ['html', 'css', 'javascript', 'react'],
}
for persons,skills in developer_skills.items():
        print(f"\n{persons.title()} knows the following Technologies:")
        for skill in skills:
            print(f"{skill.title()}")

print("\n")

# 3)The Student Exam Log
student_grades = {
    'arun': [75, 82, 90],
    'deepa': [95, 88, 92, 98],
    'karan': [55, 62],
}
avg_score=0

for students,marks in student_grades.items():
    #   for mark in marks:
            avg_score=sum(marks)/len(marks)
            if avg_score >= 80:
                    print(f"\n{students.title()} has an avg score of {avg_score} - Status: Passed with Disinction!")
            else:
                    print(f"\n{students.title()} has an avergae of {avg_score} - Status : Passed")

print("\n")

# 2) The Topping Counter
pizza_order = {
    'crust': 'thin',
    'size': 'large',
    'toppings': ['mushrooms', 'extra cheese', 'onions'],
}
current_topping = pizza_order['toppings']
current_topping.append('jalapenos')
current_topping.append('olive')
print(current_topping)                 # NOTE: Same O/P !!REMEMBER
print(pizza_order['toppings'])         # NOTE: Same O/P.!!REMEMBER

if 'mushrooms' in pizza_order['toppings']:
        print(f"'mushrooms' detected: adding garlic butter.")
print(f"Your {pizza_order['size']} Pizza has {len(pizza_order['toppings'])} topping.")

for topping in pizza_order['toppings']:
        print(f"Adding: <{topping}.>")