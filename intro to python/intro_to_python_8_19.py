
spiderman = "Peter Parker" # string
num_of_hats = 5 # int - whole number
currency = 5.99 # float - decimal / floating point number

is_hot = True # bool - boolean
is_cold = not False

# list - mutable, ordered, indexable, allows duplicates
makeup = ["Fenty", "Pat McGrath Labs", "Mented"]
makeup.append("Juvias Place")
makeup.append("Beauty Bakerie")

makeup[0] = "Danessa Myricks Beauty"
#print(makeup[4])

#print("length of variable makeup", len(makeup))

# tuple - immutable, indexable, ordered, allows duplicates
languages = ("French", "Spanish", "Greek", "Italian", "Hmong", "Hindi")
#print(languages[0])

# sets - mutable, not indexable, not ordered, does not allow duplicates
luxury_bags = {"Telfar", "Coach", "Chanel", "Michael Kors", "Gucci"}
luxury_bags.add("Kurt")
luxury_bags.add("Coach")

new_bag = "Fendi"

if "Ferregamo" in luxury_bags:
    print("do not buy another bag")
elif new_bag not in luxury_bags:
    luxury_bags.add(new_bag)
else:
    luxury_bags.add("Ferregamo")
    print("you bought another bag")

#print(luxury_bags)

#dictionary - curly braces,
spongebob_characters = {"Spongebob":"sponge",
                        "Squidward":"squid",
                        "Sandy":"squirrel",
                        "Gary":"snail",
                        "Patrick":"starfish",
                        "Mr. Krabs": "crab",
                        "Plankton":"plankton"}

# for character, animal_type in spongebob_characters.items():
#     print(f"{character} is a {animal_type}")

# print(spongebob_characters.items())


import csv
import pprint

with open('../.venv/Scripts/cheese_details.csv', 'r', newline='', encoding="UTF-8") as csvfile:
    reader = csv.reader(csvfile)
    current_line = next(reader, None)

    types_of_cheese : dict = {}

    count = 0
    try:
        while current_line is not None:

            if(current_line[2] in types_of_cheese):
                types_of_cheese[current_line[2]] += 1
            else:
                types_of_cheese[current_line[2]] = 1

            current_line = next(reader, None)
    except:
        print("Error")

pprint.pprint(types_of_cheese)















































