# Functions using positional arguments

def describe_pet(pet_name, animal_type="dog"):
    """"Display infromation about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "wille")

# showing  the order of arguments mater using positional arguments

describe_pet("harry", "hamster")

# functuons using Keyword arguments

describe_pet(animal_type="hamster",pet_name="harry")

# using default values

describe_pet(pet_name="willie")