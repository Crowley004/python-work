# Using the range() function to generate a series of numbers.

for value in range(1, 5):
    print(value)
# The range() function will stop at the value befor the max in the range.

for value in range(1, 6):
    print(value)

# You can make a list of numbers by wraping the list() function around the range().

numbers = list(range(1, 8))
print(numbers)

# working on tiy 4-10, add the following steps.

msg = ("the first three items on the list are:")

print(msg)
print(numbers[1:4])

msg = ("\nThree items frome the middle of the list are:")

print(msg)

print()
print(numbers[3:6])

msg = ("\nThe last three items on the list are:")

print(msg)
print(numbers[4:])

# using a third number in range to skip over numbers.

even_numbers = list(range(2, 11, 2))
print(even_numbers) 

