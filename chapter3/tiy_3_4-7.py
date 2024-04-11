# Make a guest list of at least 3 people and print a message to each, enviting them to dinner.

guest_list =['greg', 'bob', 'jim']

msg = f'{guest_list[0].title()} would to like to join us for dinner'
print(msg)
msg = f'{guest_list[1].title()} would to like to join us for dinner'
print(msg)
msg = f'{guest_list[2].title()} would to like to join us for dinner'
print(msg) 

# Print who can't make it to dinner.

popped_gust = guest_list.pop(2)

print (f"\n{popped_gust.title()} sadly can't make it to dinner.")

# Invite three new guests.
