# make a list of pizzas and use for loop to print each.

pizzas = ['philly','chicken and spinach','pepperoni']

for pizza in pizzas:
    print(pizza)

# Now say I like each pizza.

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!") 

print("I just really love pizza!")

# Working from tiy 4-11.

# First copy list over to friends_pizzas.

friends_pizzas = pizzas[:]

# Next add new pizza to original list.

pizzas.append("ham and mushroom")

# Now add pizza oto friends list.

friends_pizzas.append("pineapple")

# Now print each list to prove the they are separate.
# first using for loop.
msg =("\nMy favorite pizzas are:")

print(msg)
for pizza in pizzas:
    print(pizza)

msg = ("\nMy friend's favorite pizza are:")

print(msg)
for pizza in friends_pizzas:
    print(pizza)
# Make a list of animals.  
animals = ["dog","cat","fish"]

# Make a statement about the animals.

for animal in animals:
    print(f"\nI think {animal} would make a great pet.")

print("Any of these beasts would make great pets.")
