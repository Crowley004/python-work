# 5-6
# Use if-elif-else chain that determins a person's stage of life.

age = input('What is your age? ')

age = int(age)

if age < 2:
    print('you are a baby.')

elif age < 4:
    print('You are a toddler.')

elif age < 13:
    print('You are a kid.')

elif age < 20:
    print('You are a teenager.')

elif age < 65:
    print('You are an adult.')
    
else:
    print('You are an elder.')
