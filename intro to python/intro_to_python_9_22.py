
childrens_book = "Where the Wild Things Are" # string - text
num_of_books = 52 # int - whole number
cost = 9.99 # float - floating point number

# list, tuples, sets

# list - ordered, indexable, mutable, allow duplicates
flowers = ["daisy", "lily", "rose", "sunflower", "tulips", "hibiscus"]
# print(flowers)
# flowers.append("gerber")
# print(flowers)
# flowers.remove("rose")
# print(flowers)
# flowers.append(1)
# print(flowers)
# flowers[0] = "orchid"
# print(flowers)

# tuples - ordered, indexable, not mutable, allows duplicates
fragrances = ("jasmine", "peach", "vanilla", "wood", "cedar", "cherry")
# print(fragrances[0])

# set - unordered, not indexable, mutable, do not allow duplicates
cars = {"BMW", "Toyota", "Honda", "Audi", "Bugatti"}

# cars.add("Ford")
# print(cars)
# cars.add("Toyota")
#
# sorted_cars = sorted(cars)
# print(sorted_cars)

# dictionary - key/value pairs
star_signs = {"Virgo": "Matcha",
              "Scorpio": "Lemonade",
              "Libra": "Strawberry Milk",
              "Pisces": "Coffee",
              "Aries": "Redbull",
              "Capricorns": "Rootbeer",
              "Leo":"Pineapple Juice"
              }

star_signs["Gemini"] = "Chai Latte"

# for sign, drink in star_signs.items():
#     print(f"{sign} likes to drink {drink}")



inventory = input("What is your current inventory? ") # number of hats

print(isinstance(inventory, float))


if inventory >= 50:
    print("You need to sell more hats!")
elif inventory >= 30:
    print("You are getting low on hats!")
elif inventory >= 20:
    print("You need to purchase more hats")
else:
    print("You don't have enough hats left")





















