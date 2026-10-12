# While Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1

print("\n")

prompt = '\nTell me something, I will repeat it back to you'
prompt += '\nEnter "quit" to end the progress : '
message = ' '
while message != 'quit':
    message = input(prompt)
    print(message)