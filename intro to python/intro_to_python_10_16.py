title = "Princess Bride" # string
year = 1987 # int - whole number
cost = 19.99 # float - floating point number
isTired = True

# list, tuple, set

# list - ordered, indexable, mutable, allows duplicates
colors = ["red", "purple", "blue", "magenta","blue"]
colors[0] = "orange"
# print(colors)

colors.append("violet") # add to the end of the list
colors.remove("purple")
# print(colors)

#tuple - ordered, indexable, not mutable, allow duplicates
flowers = ("sunflower", "roses", "tulips", "peonies")
# print(flowers)
# print(flowers[-4])

# ChopSuey - Link up on Discord in currently on Lists, Dicts, there are some areas where I just get confused.
# Github class
# it’s the harvard course and it’s free ! the problem sets go with the course but you can access them - CS50 problems

# singli line comment

"""
This is a multiline comment
So you can have multiple comments
within the quotes
"""

x = 5
x += 1 # is the same as x + 1
# print(x)

# set - unordered, not indexable, mutable, no duplicates
animals = {"cat","dove","wolf","gopher"}

# animals.add("elephant")
# print(animals)
#
# if "cat" in animals:
#     print("Yes, there is a cat!")


characters = {"Mikey":"Pizza",
              "Momo":"Peaches",
              "Garfield":"Lasagna",
              "Scrat": "Nut",
              "Homer": "Donuts"}

# for character,food in characters.items():
#     print(f"{character.lower()} loves to eat {food.endswith("s")}")
#
# num_of_slices = int(input("How many slices did you eat? "))


def getPizzaMessage(slices):
    if slices <= 0:
        return "You didn't eat any pizza!"
    elif slices < 10:
        return "You didn't eat much pizza"
    else:
        return "You ate a whole lot of pizza!"


# print(getPizzaMessage(num_of_slices))

percentage = 0.021457542142

# print(f"Your percentage is {percentage:.2f}")


#result = 89 * .02

#value = 12

# if value % 2 == 0:
#     print(f"{value} is even")

import random

options = ("rock", "paper", "scissors")

value = random.randint(0,100)

result = value % 3
if result == 0:
    print(options[0])
elif result == 1:
    print(options[1])
else:
    print(options[2])


# We're not programming, we're just chatting now


































