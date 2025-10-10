name = "spiderman" # string - text
whole_number = 5 # int - whole number
cost = 5.99 # float - floating point number

is_cold = False # boolean

# list, tuples, sets

# lists - ordered, indexable, mutable, allow duplicates
fruits = ["orange",
          "apple",
          "kiwi",
          "pear",
          "grapes"]

fruits[1] = "coconut"
fruits.append("watermelon")
fruits.remove("orange")
del fruits[0]
# print(fruits)


# tuple - ordered, indexable, not mutable, allow duplicates
shapes = ("diamond",
          "triangle",
          "square",
          "rhombus",
          "oval",
          "circle")

#print(shapes[0])


#set - not ordered, not indexable, mutable, does not allow duplicates
flowers = {"tulip", "poppy", "lily", "lilac", "roses"}
flowers.remove("tulip")

# if "tulip" in flowers:
#     print("Yes, the flowers list has a tulip")
# else:
#     print("No, there are no tulips here")

# dictionary - hashmap key/value pairs
starsign_drinks = {"cancers":"tequila",
                   "leo":"boba",
                   "aries": "apple juice",
                   "scorpio": "matcha",
                   "taurus": "ice tea"}

for sign, drink in starsign_drinks.items():
    print(f"{sign} loves to drink {drink}")



