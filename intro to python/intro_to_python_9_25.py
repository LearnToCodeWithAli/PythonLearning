title = "Surf's Up"  # string - text
year = 2007  # int - whole number
ticket_cost = 14.99  # float - floating point number

# list, tuples, sets

# list - ordered, indexable, mutable, allows duplicates
flowers = ["roses", "tulips", "peonies", "gardenias", "dandelion", "roses"]

# print(flowers[0])
# flowers.append("hyacinth")
# print(flowers)
# print(flowers[-1])
# flowers.remove("peonies")
# print(flowers[::-1])
# del flowers[0]
# print(flowers)

# tuples - ordered, indexable, not mutable, allow duplicates
fragrances = ("jasmine", "sandalwood", "rosemary", "vanilla", "lilac", "eucalyptus", "lilac")
# print(fragrances[2])
# print(fragrances)

# set - not ordered, not indexable, mutable, do not allow duplicates
drinks = {"tea", "coke", "matcha", "horchata", "juice", "milkshake", "coffee"}
drinks2 = {"tea", "coke", "matcha", "horchata"}

# print(drinks <= drinks2)
# drinks.add("rootbeer")
# drinks.remove("tea")
# print(len(drinks))
# drinks.add("coffee")
# print(len(drinks))

# list - ordered, indexable, mutable, allows duplicates
# tuples - ordered, indexable, not mutable, allow duplicates
# set - not ordered, not indexable, mutable, do not allow duplicates

# dictionaries - key/value pairs

birth_month = {"January": "Mouse",
               "February": "Dog",
               "March": "Worm",
               "April": "Cow",
               "May": "Dinosaur",
               "June": "Bobcat"}

flowers = ["roses", "tulips", "peonies", "gardenias", "dandelion", "roses"]
people = ["ann", "joel", "jace", "dari", "luna", "charles"]

flowers_to_people = dict(zip(people, flowers))

# for each in flowers_to_people:
#     print(each)
#
# print(flowers_to_people)

# for person, flower in flowers_to_people.items():
#     print(f"{person} buys {flower} for Tommy's graduation")

# person_name = input("What is the main character's name? ")
# location = input(f"Where was {person_name} going? ")
# action = input(f"What did {person_name} do instead? ")
#
# template = f"""\n{person_name} was going to {location}.
# They needed to buy eggs for their grangran.
# Instead, they {action}.
# Grangran was not happy with them."""
#
# print(template)

# count = 3
# while count <= 5:
#     count += 1
#     print(count)

listy = []

# index = 1
#
# squares = [i**2 for i in range(10)]
# print(squares)

# items = list(range(5))
result = [i for i in range(5) if i > 2] # this is incorrect, check the syntax
print(result) #
