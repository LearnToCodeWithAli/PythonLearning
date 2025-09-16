recipe = "deep dish pizza" # string
num_of_pizzas = 15 # int - whole number
cost_of_pizza = 19.99 # float

# print(round(num_of_pizzas * cost_of_pizza,2))


# list, tuple, set



#tuple - indexable, ordered, not mutable, allows duplicates
colors = ("blue","red","yellow","purple", "red")
# print(colors[0])
# print(colors)

# set - not indexable, not ordered, mutable, does not allow duplicates
destinations = {"Miami", "Seattle", "Los Angeles", "New York"}
destinations.add("Chicago")
destinations.remove("Miami")
# print(destinations)

star_signs = {"Virgo":"Coconut Water",
              "Cancer":"Matcha",
              "Taurus":"Black Coffee",
              "Gemini":"Espresso"}


# for sign, drink in star_signs.items():
#     print(f"{sign} drinks")
#     print(drink)

speed = 60


# if speed >= 50:
#     print("You're going too fast")
# if speed >= 35:
#     print("You're going the speed limit")
# else:
#     print("You are going to slow")


import random

#list - indexable, ordered, mutable, allows duplicates

fruits = ["kiwi", "grapefruit", "pineapple","banana","pomelo"]
fruits.append("pineapple")
print(fruits.remove("kiwi"))
#print(fruits[0])
# print(fruits)

for fruit in fruits:
    random_integer = random.randint(1, 10)
    print(f"{fruit} {random_integer}")



