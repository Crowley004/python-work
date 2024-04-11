# basic list
biycycles = ['trek', 'cannondale', 'redline', 'huffy', 'specialised']
print(biycycles)

# how to pull a item from a list using index.
print(biycycles[0])

# an index starts at zero.

# To access the last element in a list use index [-1]
print(biycycles[-1])

# You can use formatting methods on lists as well.
print(biycycles[3].title())

# Pulling an item from a list and adding to a variable.
msg = f"My first bike was a {biycycles[3].title()}."
print(msg)
