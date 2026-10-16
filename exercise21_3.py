# 3)Dream Vacation
dream_prompt = '\nIf you could visit one place in the world, PRESS "done" to stop'
dream_prompt += '\nWhere would you go : '
dream_vacation = []
active = True

while active:
    vacation = input(dream_prompt)
    vacation = vacation.lower() 
    if vacation == 'done':
        active = False
    else:
        dream_vacation.append(vacation.title())

for dream in dream_vacation:
    print(dream)