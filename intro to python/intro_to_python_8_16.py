

katara = "I am a waterbender" # string
whole_number = 5 # int
floating_number = 4.5 # float - floating point number / decimal number

isHappy = False

# if isHappy:
#     print("I am happy")
# else:
#     print("I am sad")

# lists - mutable, ordered, indexable, allow duplicates
atla_characters = ["katara","sokka","aang","toph"]

# print(atla_characters[0])
atla_characters[0] = "azula"

atla_characters.append("katara")
atla_characters.remove("azula")
# print(atla_characters)

# tuples - immutable, ordered, indexable, allow duplicates
countries = ("US", "JP","MX","AR","SP", "DR", "DR")
# print(countries)
# print(countries[1])

# set - mutable, unordered, not indexable, does not allow duplicates
companions = {"appa", "momo", "naga","pabu"}
# print(companions)
# print(companions[0])

friend = "flopsie"
companions.add(friend)

# for i in range(15):
#     print(i, end = " ")

#dictionary - key:value pairs
pokemon = {"bulbasaur":"leaf blade","charmander":"flame thrower","squirtle":"water gun"}

for name, move in pokemon.items():
    print(f"{name} uses {move}")