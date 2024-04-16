# Using the range() function to generate a series of numbers.

for value in range(1, 5):
    print(value)
# The range() function will stop at the value befor the max in the range.

for value in range(1, 6):
    print(value)

# You can make a list of numbers by wraping the list() function around the range().

numbers = list(range(1, 6))
print(numbers)

# using a third number in range to skip over numbers.

even_numbers = list(range(2, 11, 2))
print(even_numbers) 
