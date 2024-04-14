# use a variable to represnt a person's name, and then print a message to that person.

user_name = "Bobby Hill"
print (f"Hello {user_name}, can I see your purse?")

# use a variable to represnt a persons name and then print the name in lower upper and title case.

user_name = "Bobby Hill"
print(user_name.upper())
print(user_name.lower())
print(user_name.title())

# print a quote from a famous person.

print('Diamond Dallas Page once said, "You can\'t control what happens to you, but you can control how you react to it."')

# repeat last but use variable for name.

famous_person = "Diamond Dallas Page"

print(f'{famous_person} once said, "You can\'t control what happens to you, but you can control how you react to it."')

# use a variable for a persons name and add whitespace on both sides. print the name as is and with eace strip fuction. I needed a lot of help with this one.:(

jobber = "\tTrevor Crowell\n"

print("Unmodified:")
print(jobber)

print("\nUsing lstrip():")
print(jobber.lstrip())

print("\nUsing rstrip():")
print(jobber.rstrip())

print("\nUsing strip():")
print(jobber.strip())

# use the removesuffix() method on a variable.

filename = "python_notes.txt"

print(filename)
simple_filename = filename.removesuffix(".txt")
print(simple_filename)
