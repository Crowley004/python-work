# An example of a if-elif-else syntax.

age = input('What is your age? ')

a = int(age)

if a < 4:
    print('Your admission cost is $0.')

elif a < 18:
    print('Your admission cost is $25.')

else:
    print('Your admission cost is $40.') 
