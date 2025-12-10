print('What is your name')
name=input()
if len(name)< 3:
    print('Name must be at least 3 characters long')
elif len(name)>50:
    print('Name can have max 50 characters')
else:
    print('Name looks good')

