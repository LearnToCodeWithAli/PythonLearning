# Refs: W3Schools and Python docs, GeeksForGeeks, Baeldung, TutorialsPoint, LearnPython.org

# studio ghibli

main_character = "Chihiro" # string
chihiro_age = 11 # int
number_of_meals = 12.5 # float

isHungry = True
isHappy = False

# list, set, tuples

# list - ordered, mutable, indexable, and can have dupes
characters = ["Chihiro", "Haku", "Yubaba"]

# print(characters[-3])
# print(characters[0])

characters.append("Zeniba")
# print(characters)

characters[0] = "Kamaji"
# print(characters)
characters.remove("Kamaji")
# print(characters)

# print(characters.pop())
# print(characters)


# print(movies)
# print(movies[0])

#test = {[1,2,3], [2,3,1]}
# print(test)



# list - ordered, mutable, indexable, and can have dupes
characters = ["Chihiro", "Haku", "Yubaba"]

# set - unordered, mutable, not indexable, cannot have duplicates
movies = {"Spirited Away", "Howl's Moving Castle", "Kiki's Delivery Service", "My Neighor Totoro"}

movies.add("Spirited Away")
movies.add("Whisper of the Heart")

# print(movies)
# tuple - ordered, immutable, indexable, can have duplicates
passwords = ("1password", "123password", "PassWord1", "QWERTY")

# Refs: W3Schools and Python docs, GeeksForGeeks, Baeldung, TutorialsPoint, LearnPython.org

def doNotBuyMovie():
    print("Do not buy the movie. You already have it")

# if "Spirited Away" in movies:
#     doNotBuyMovie()

characters = {"Chihiro", "Haku", "Yubaba", "Goku"}
atla = {"Sokka", "Katara", "Aang", "Toph", "Goku"}

#print(characters.union(atla))
#print(characters.intersection(atla))
#print(characters.difference(atla))

import pprint

# dictionary - key/value pairs
meals = {"breakfast":"waffles", "lunch":"turkey sandwich", "dinner":"pasta salad"}

# print(meals["breakfast"])
meals["brunch"] = "crepes"

# pprint.pprint(meals)

# for mealtime, food in meals.items():
#     print(f"I'm going to eat {food}")


# time_of_day = "breakfast"
#
# match time_of_day:
#     case "breakfast":
#         print(f"I eat {meals[time_of_day]} at 8am")
#     case "lunch":
#         print(f"I eat {meals[time_of_day]} at 12pm")
#     case "dinner":
#         print(f"I eat {meals[time_of_day]} at 8pm")


# grade = 90
#
# if grade >= 90:
#     print("You did amazing!")
# elif grade >= 80:
#     print("You still did amazing!")
# elif grade >= 70:
#     print("You did amazing but you need to study")
# else:
#     print("You really need to study")


characters = {"Chihiro", "Haku", "Yubaba", "Goku"}




# for index, element in enumerate(characters):
#     print(f"at {index} is {element}")
#     print("hi")







# Refs: W3Schools and Python docs, LearnPython.org, GeeksForGeeks, Baeldung, TutorialsPoint


indices = []











