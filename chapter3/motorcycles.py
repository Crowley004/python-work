motorcycles = ['honda', 'yamaha', 'suziki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ["honda", "yamaha", "suziki"]
# add to the end of a list.
motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append("honda")
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.append("suzuki")
print(motorcycles)
# How to insert anywhere in a list.
motorcycles.insert(0, "ducati")

print(motorcycles)

# How to remove a item

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# How to pop off the last item in a list to use for later.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping off a set item off a list 
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)

print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Using the .remove method 
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")