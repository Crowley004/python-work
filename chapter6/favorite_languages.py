# a dictionary of similar objects
  
favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward':'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using a for loop to get key-values.

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")
    
# Using the .key() method. 

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')

# Checking to see if a key id in the dictionary.

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# Looping through a dictionary's keys in a particular order.

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

# Using the .values() method.
# Wrap a set() function around a collection to stop duplicates.
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

# Make a list of coders and check them agist people who took the poll.

programmers = ['steve', 'roman','cody','jen', 'phil', 'sarah']

for programmer in programmers:
    if programmer in favorite_languages.keys():
        print(f'Thank you for taking the poll {programmer.title()}.')
    else:
        print(f'Please take the poll {programmer.title()}.')

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
        print(f"\t{language}")
    else:
        print(f"\n{name.title()}'s favorite languaes are:")
        for language in languages:
            print(f"\t{language.title()}")