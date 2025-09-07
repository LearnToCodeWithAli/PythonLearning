
candle_scent = "orange blossom" # string - text
num_of_candles = 20_000 # int - whole number
gallons_of_gas = 5.6 # float -  floating point number

# tuple, set, list

# list - ordered, mutable, indexable, allows duplicates
favorite_movies = ["Devil Wears Prada", "Kung Fu Panda", "Ice Age"
                   "Finding Nemo"]
#print(favorite_movies[0])

# tuple - ordered, not mutable, indexable, allow duplicates
citrus = ("lemon", "orange", "tangerine", "lime")
#print(citrus[0])

# set - not ordered, mutable, not indexable, do not allow duplicates
companies = {"hp", "mac", "toshiba", "sony", "intel", "acer"}
companies.add("lenovo")
#print(companies)
companies.remove("mac")
#print(companies)



#dictionary - key/value pairs
cars = {"January":"Ford", "February":"Dodge", "March":"Audi",
        "April":"Mistubishi"}

# for month, car in cars.items():
#     print(f"If you were born in {month} then you will buy a {car}")

"Harry said to Simon, \"We're not friends anymore\""



def print_quote():
    name = "Jeremy"
    age = 15
    height = 62

    return "Hello, %s! You are %d years old and %.2f meters tall." % (name, age, height)#

#print(formatted_string)


class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        return f"I am {self.name} and I am {self.age} years old"


cat = Animal("Fluffy", 3, 10)
print(cat.speak())


# Do you do spatial python? I’m trying to learn ArcPy for ArcGIS
# jetstreamin




# learnpython.org, codeacademy, W3Schools, GeeksForGeeks, Baeldung