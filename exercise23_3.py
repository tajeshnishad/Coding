# 1) Messeges 
txt_msg = ['hello there!','how are you','how are you doing','is your family doing all okay!?']

def txt_messeges(msgs):
    for msg in msgs:
        print(msg)

txt_messeges(txt_msg)

print("\n")

# 2) Sending messeges 
txt_msgs = ['Hello there!','How are you','How are you doing','Is your family doing all okay!?']
send_msgs = []

def messeges(txt_messeges,send_messeges):
    while txt_messeges:
        current_msg = txt_messeges.pop()
        send_messeges.append(current_msg)

def sent_messeges(send_messeges):
    for send_messsege in send_messeges:
        print(send_messsege)

messeges(txt_msgs,send_messeges=send_msgs)
print("\n")
print("Printing all messeges that has been sent")
sent_messeges(send_msgs)
print(f"1st data was stored here: {txt_msgs}")
print(f"1st data was stored here: {send_msgs}")

print("\n")

# 3) Archived messeges 
txt__msgs = ['Hello there!','How are you','How are you doing','Is your family doing all okay!?']
send__msgs = []

def messeges_(txt_messeges,send_messeges):
    while txt_messeges:
        current_msg = txt_messeges.pop()
        send_messeges.append(current_msg)

def sent_messeges_(send_messeges):
    for send_messsege in send_messeges:
        print(send_messsege)

messeges_(txt__msgs[:],send__msgs)
sent_messeges_(send__msgs)
print(f"1st data was stored here: {txt__msgs}")
print(f"1st data was stored here: {send__msgs}")