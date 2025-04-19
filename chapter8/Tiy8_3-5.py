# 8_2 - 8_4
def make_shirt(message= "I love python!", size="large"):
    print(f"A {size} shirt has been ordered with {message} on it.")

make_shirt("5xl", "I am fat")
make_shirt(message="what the hell", size="small")

make_shirt(size="medium", message="cat poop")

# 8_5
def describe_city(city, country="America"):
    print(f"{city.title()} is a city in {country.title()}.")

describe_city("springfield")
describe_city("london", "england")
describe_city("boston")
