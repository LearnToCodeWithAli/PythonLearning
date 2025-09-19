
movie_title = "Surf's Up" # string
year = 2012 # int - whole number
ticket_cost = 15.99 # floating point number

# list, tuples, sets

# list - indexable, ordered, mutable, allow duplicates
constellations = ["little dipper",
                  "big dipper",
                  "orion",
                  "sagitarius"]

# constellations.append("acrux")
# print(constellations)
# constellations.remove("orion")
# print(constellations)

# print(constellations[0])
# constellations[0] = "sirius"
# print(constellations)
#
# print(constellations[::-1])
# print(constellations[2:3])

# tuple - ordered, indexable, allows dupes, immutable
animals = ("lions", "tigers", "bears", "oh my")
#print(animals[0])

# set - not ordered, not indexable, do not allow dupes
# are mutable
fruits = {"dragonfruit", "lychee","papaya","kiwi"}
# print(fruits)
#
# fruits.add("durian")
# print(fruits)
# fruits.remove("kiwi")
# print(fruits.pop())
# print(fruits)
# fruits.add("lychee")
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# for index in range(5):
#     print(index)


# isHot = True
#
# if not isHot:
#     print("Do not drink")


speed = int(input("How fast were you going? "))

if speed > 15:
    print("You are going too fast!")
elif speed > 10:
    print("You are going the speed limit")
else:
    print("You are going too slow")







