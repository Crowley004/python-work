# Tuples use parentheses instead of square brackets.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Trying to change an item in the tuple.

# dimensions[0] = 250

# Looping through all values in tuples.
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Writing over a tuple.
print("\nModified dimensions:")

dimensions = (400, 100)

for dimension in dimensions:
    print(dimension)