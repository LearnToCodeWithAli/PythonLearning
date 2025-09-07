# 1 data types, string functions, conditionals, loops, methods, classes
# References: W3Schools and Python documentation

doggo = "happy"

numOfToes = 10  # int
balance = 233.50  # float

snorlax = [1, 2, 3, 4, 5, 5, 4]  # list
coordinates = ("x", "y", "z")  # tuple
books = {"Alice in Wonderland", "Pride and Prejudice", "Cat in the Hat", "Cat in the Hat"}  # set

snorlax_set = set(snorlax)

# print(books)
# print(snorlax_set)

# avatar_characters = {"Katara": 15,
#                      "Sokka": 16,
#                      "Aang": 11,
#                      "Zuko": 16,
#                      "Toph": 12}

def print_avatar_character_ages(avatar_characters):
    for name, age in avatar_characters.items():
        print(f"{name} is {age} years old")
        print(name + " is " + str(age) + " years old")

        this_is_a_string = "{char_name} is {char_age} years old"
        print(this_is_a_string.format(char_name=name, char_age=age))

        this_is_another_string = "{0} is {1} years old"
        print(this_is_another_string.format(name,age))

#print_avatar_character_ages(avatar_characters)

# 1 data types, string functions, conditionals, loops, methods, classes
# References: W3Schools and Python documentation


#air > water > earth > fire > air

# from enum import Enum
#
# class BendingType(Enum):
#     AIR   = 4
#     WATER = 3
#     EARTH = 2
#     FIRE  = 1
#
#
# avatar_characters = {"Katara": BendingType.WATER,
#                      "Aang": BendingType.AIR,
#                      "Zuko": BendingType.FIRE,
#                      "Toph": BendingType.EARTH}
#
# #opponent1 vs 2
# opponent = BendingType.FIRE
#
# for name, bending in avatar_characters.items():
#     if bending == BendingType.WATER and opponent == BendingType.FIRE:
#         print(f"{name} wins the fight!")
#     if bending == BendingType.WATER and opponent == BendingType.FIRE:
#         print(f"{name} wins the fight!")