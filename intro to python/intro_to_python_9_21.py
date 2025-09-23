# data types, data structures, conditionals, loops, classes, methods

name = "appa" # string - text
viewers = 11 # int - whole number
cost = 9.99 # floating point number

# lists, tuples, sets

# list - ordered, indexable, mutable, allows duplicates
cupcakes = ["vanilla", "chocolate", "strawberry", "red velvet"]

# cupcakes[0] = "yellow"
# cupcakes.append("lemon")
# print(len(cupcakes))
# del cupcakes[0]
# print(cupcakes)

# print(len(cupcakes))
#
# for cupcake in cupcakes:
#     print(cupcake)


#tuples - ordered, indexable, not mutable, allows duplicates
fruits = ("apple", "banana", "cherry", "tomato", "mango", "orange", "kiwi")
# print(fruits)

# set - unordered, not indexable, mutable, do not allow duplicates
flavors = {"jasmine", "passion fruit", "strawberry", "lime", "mint", "cherry"}
print(flavors)
flavors.add("watermelon")
flavors.add("jasmine")
print(flavors)