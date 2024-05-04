# Make a dictionary of five python terms and print.

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A set of items in a particular order.',
    'loop': 'Work through a set of items, one at a time.',
    'dictionary': "A set of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

word = 'string'
print(f"\n{word}: {glossary[word]}")

word = 'comment'
print(f"\n{word}: {glossary[word]}")

word = 'list'
print(f"\n{word}: {glossary[word]}")

word = 'loop'
print(f"\n{word}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word}: {glossary[word]}")

#  Now to clean up the code.

for word, definition in glossary.items():
    print(f'{word.title()}: {definition}')