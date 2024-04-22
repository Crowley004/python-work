# 5 8-9
# Make a list of five including the admin and print a greeting to each.

# users = ['Jim', 'greg', 'cory', 'mike', 'admin']
users = []

for user in users:
    if user == 'admin':
        print('Welcome back admin, would you like to see the staus report?')
    elif  user in users:
        print(f'Welcome back {user}.')
# add if statement to check if they had any active users.

if  users == []:
     print('Did everyone call of today?')