current_users = ['eric', 'jim', 'Steve', 'greg', 'Dave']
new_users = ['cathy', 'Jim', 'PHIL', 'ricky', 'Eric']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Bummer {new_user}, that name is taken.")
    else:
        print(f"Neat, {new_user} is still available.")