# First for loop.
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

# Now used with a formated string.

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print('\nThank you, everyone. That was a great magic show!')



