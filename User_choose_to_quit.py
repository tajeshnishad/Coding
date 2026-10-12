# Users choose when to Quit
prompt = '\nTell me something, I will repeat it back'
prompt += '\nPlease enter the message : '
message = ' '
while message != 'quit':
    message = input(prompt)
    print(message)

print("\n")

# User choose to qit without print it at last
promp = 'Tell me something, I will print it back to you. '
promp += '\nPlease enter tne message : '
messag = ' '
while messag != "quit":
    messag = input(promp)
    if messag != 'quit':
        print(messag)