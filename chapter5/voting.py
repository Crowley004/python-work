# Check if  person is old enough to vote.
print('Let\'s see if your old enough to vote.')
age = input('What is your age? ')
a = int(age)

if a >= 100:
    print('LIAR!!!!')
    quit()

elif a >= 18:
    print('You are old enough to vote.')
    q = input('Have you registered to vote yet? ')

else:
    print('You are too young to vote.')
    print('please register to vote as soon as you turn 18.')
    quit()

# This is for the if they are registered or not.
if q == 'yes':
    print('Outstanding!')

else:
    print('Pitter-patter, let\'s get at\'er.')