# # Use a for loop to print 1 to 20
# num = []
# for value in range(1,21):
#     num.append(value)

# print(num)

# # Make a list from 1 to 1 million and print.

# million = list(range(1000001))
# for num in million:
#     print(num)
# # Use the sum(), min() and max() functions.

# print("\n")

# print(sum(million))

# print("\n")

# print(min(million))

# print("\n")

# print(max(million))

# Make a list from 1 to 20 and print odd numbers.

odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
 print(number)

#  Make a list  of the multiples 3, frome 3 to 30. Use a for loop and print.

three = list(range(3, 31, 3))

for num in three:
 print(num)

# Make a list of the first 10 cubes and print with a for loop.

cubes =[]
for value in range(1, 11):
 cube = value ** 3
 cubes.append(cube)

print(cubes)

cubes = []
for value in range(1, 11):
 cubes.append(value**3)

print(cubes)

# Repeat last exercise using list comprehension.
print("\n")
cubes = [cube ** 3 for cube in range(1, 11)]
print (cubes)