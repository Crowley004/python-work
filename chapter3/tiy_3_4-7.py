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

print('\nI am just letting everone know that we will be move the dinner party to a bigger location')

guest_list.insert(0, 'dave')
guest_list.insert(2,'john')
guest_list.append('bill')
print(guest_list)

#  Print new gust invites.

msg = f'{guest_list[0].title()} would to like to join us for dinner?\n'
print(msg)
msg = f'{guest_list[1].title()} would to like to join us for dinner?\n'
print(msg)
msg = f'{guest_list[2].title()} would to like to join us for dinner?\n'
print(msg)
msg = f'{guest_list[3].title()} would to like to join us for dinner?\n'
print(msg)
msg = f'{guest_list[4].title()} would to like to join us for dinner?\n'
print(msg) 

# Now i have to dissinvite all but two people for some reason.

msg = ('\nDo to unforseen circumstances we can only have two people for dinner.')
print(msg)

# Use the pop() method to remove all but two guests.

popped_guest = guest_list.pop()
msg = f'Sorry {popped_guest.title()} you have been voted off the island!\n'
print(msg)

popped_guest = guest_list.pop()
msg = f'Sorry {popped_guest.title()} you have been voted off the island!\n'
print(msg)

popped_guest = guest_list.pop()
msg = f'Sorry {popped_guest.title()} you have been voted off the island!\n'
print(msg)

msg = f"I'm happy to inform you {guest_list[0].title()} that you are still welcome"
print(msg)

msg = f"I'm happy to inform you {guest_list[1].title()} that you are still welcome"
print(msg)

# del() the last two.

del guest_list[0]
del guest_list[0]

print(guest_list)