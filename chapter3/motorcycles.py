# Make a list of motorcycles.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Now change the first index of the list with a new value.

motorcycles[0] = 'ducati'
print(motorcycles)

# Add a value to the list using the append() method.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Start from an empty list and append all.

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Add to list at any index by using the insert() method.
# In the parentheses add the index and then the value.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# ['ducati', 'honda', 'yamaha', 'suzuki']

# Remove a index by using the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles)
# ['yamaha', 'suzuki']

# Using the pop() method to remove the last index of a list to use later.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Popping any items from a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'\nThe first motorcycle I owned was a {first_owned}.')

# Removing an item by value.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Use the remove() method to work with a value that's being removed from a list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')


