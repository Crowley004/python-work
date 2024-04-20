# An example of a if-elif-else syntax.

age = input('What is your age? ')

a = int(age)

if a < 4:
    price = '$0'

elif a < 18:
    price = '$25'

elif a < 65:
    price = '$40'

else:
    price ='$20'

print(f'Your admission cost is {price}.')
