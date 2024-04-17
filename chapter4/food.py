# How to copy a list.
my_foods =["pizza","falafel","carrot cake"]
friend_food = my_foods[:]

# append a new item to each list.

my_foods.append("cannoli")
friend_food.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_food:
    print(food)