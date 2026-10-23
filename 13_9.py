# Preventing a function from modifying a list 
def unrecog_users(unrec_user,recog_user):
    while unrec_user:
        current_user = unrec_user.pop()
        recog_user.append(current_user)

def recog_users(recog_user):
    for names in recog_user:
        print(names.title())

users = ['naveen','sunny','kabir','chintu','farre','mota bhai']
recognised_user = []

unrecog_users(users[:],recognised_user)
recog_users(recognised_user)

print(users)