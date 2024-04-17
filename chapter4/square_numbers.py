# making a list of the first 10 square numbers using ** for exponents.

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# to write more concisely, omit the temporary cariable square 
# and append each new value directly to the list.

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# Now buliding the same list using list comperhension:

squares = [value**2 for value in range(1, 11)]
print(squares)

# working on tiy 4-10, add the following steps.

msg = ("the first three items on the list are:")

print(msg)
print(squares[1:4])