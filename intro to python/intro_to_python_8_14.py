# Refs: W3Schools and Python docs, GeeksForGeeks, Baeldung, TutorialsPoint, LearnPython.org

gudetama = "I like soy sauce" # string - text
num_of_eggs = 12 # int - whole number
num_of_years = 2.5 # float - floating point number

# lists, sets, tuples

# list - mutable, indexable, ordered, allow duplicates
sanrio_characters = ["hello kitty",
                     "gudetama",
                     "chococat",
                     "my melody",
                     "cinnamoroll"]

sanrio_characters.append("kuromi")
sanrio_characters.remove("kuromi")
# print(sanrio_characters)

# tuple - immutable, indexable, ordered, allow duplicates
atla = ("katara", "aang", "sokka", "toph")
# print(atla[0])

# sets - mutable, not indexable, not ordered, do not allow duplicates
companions = {"appa", "momo", "naga", "pabu"}
#print(companions)
#print(type(companions))

companions.add("flopsie")
companions.add("appa")
# print(companions)
#companions[0]


# rounding
import numpy as np

x = 3.4
y = 3.6

# print(5 /2)
# print(5 // 2)
# print(5 % 2)

# print(round(x))
# print(round(y))
#
# round(x)


sailor_scouts = {}
sailor_scouts = dict()

#dictionary - key:value pairs, keys must be unique
sailor_scouts = {"Sailor Moon": "Usagi",
                 "Sailor Mercury": "Ami",
                 "Sailor Mars": "Rei"}

# for sailor, name in sailor_scouts.items():
#     print(f"{sailor} is actually named {name}")


katara = "I'm a waterbender" # string
appa = 4 # int - whole number
momo = 2.5 # float - floating point number

# list - ordered, indexable, mutable, allow duplicates
atla = ["Katara", "Sokka", "Aang", "Toph"]

# set - unordered, not indexable, mutable, no dupes
companions = {"appa", "momo", "pabu", "naga"}
# print(companions)
companions.add("flopsie")
companions.add("momo")
# print(companions)

# tuple - ordered, indexable, immutable, allow dupes
books = ("Pride and Prejudice", "Bridgerton", "Magick")
# print(books[0])




def get_beverage(star_sign):
    beverage = "water"
    match(star_sign):
        case "leo":
            beverage = "Hot Toddy"
        case "capricorn":
            beverage = "matcha latte"
        case "taurus":
            beverage = "pumpkin spice latte"
        case "virgo":
            beverage = "caramel frappe"
    print(f"Since you're a {star_sign}, then you must want a {beverage}")


#user_sign = input("What's your star sign? ")

#user_beverage = get_beverage(user_sign)


altitude = 3000

if altitude == 0:
    print("You are at sea level")
elif altitude < 500:
    print("It's very easy to breathe")
elif altitude < 3000:
    print("It's still easy to breathe")
else:
    print("You must be getting pretty cold")















