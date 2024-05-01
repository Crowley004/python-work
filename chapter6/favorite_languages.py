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