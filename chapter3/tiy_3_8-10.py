# make a list of five places I wish to travel to.

travel = ['rome','japan','washington DC','arizona','florida']
print('Here are places I would like to travel:')
print(travel)


# Use the sorted() method.

print('\nHere is the sorted list:')
print(sorted(travel))

# Print the original order.

print('\nHere is the list in the original order:')
print(travel)

# Print the list in the reverse order.

print('\nHere is the list in the reverse order:')
travel.reverse()
print(travel)

print('\nHere is the list in the original order again:')
travel.reverse()
print(travel)

# Now using the sort() method.

print('\nHere is the list in alphabetical order:')
travel.sort()
print(travel)

# Now reverse-alphbetical order.

print('\nHere is the list in reverse-alphbetical order:')
travel.sort(reverse=True)
print(travel)

# 3-9 Use the len function.

print(len(travel))

# 3-10 NO!
