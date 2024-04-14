# Make a list of cars and use the sort() method.
# The sort() method permanently sorts the list.
cars = ['bmw','audi','toyota','suburu']
cars.sort()
print(cars)

# how to use the reverse order method.
cars = ['bmw', 'audi', 'toyota','suburu']
cars.sort(reverse=True)
print(cars)

# The .sorted() method let's you display a sorted list without permanently changing the order.

cars = ['bmw','audi','toyota','suburu']

print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# Here is sorted in reverse.

print('\nHere is the list in reverse:')
print(sorted(cars,reverse=True))

# Printing a list in reverse order.

cars = ['bmw','audi','toyota','suburu']
print(cars)

cars.reverse()
print(cars)

# How to undo the reverse.

cars.reverse()
print(cars)

# finding the length of a list using the len function.

cars = ['bmw','audi','toyota','suburu']
print(len(cars))

