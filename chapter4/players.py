# How to access specific group of items in a list using slicing.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print("\n")

print(players[1:4])

print("\n")

# If you omit the first index in a slice, Python starts slice at the beginning.

print(players[:4])
print("\n")

# Omit second index in slice to go to the end of the list.

print(players[2:])
print("\n")

# you can output any slice from the end of the list using a negitve value.

print(players[-3:])
print("\n")

# You can use a slice in a for loop.

print("Her are the first three players on my team:")
for player in players[:3]:
    print(player.title())