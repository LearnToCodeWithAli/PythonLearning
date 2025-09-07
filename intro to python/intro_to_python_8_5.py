# Data types, loops, conditionals, APIs

pikachu = "pika" # string
squirtle = 7 # int
currency = 7.5 # float

# list - mutable (change values), ordered,
# allows dupes, indexed
pokedex = ["Pikachu", "Charizard", "Bulbasaur","Pikachu", "Charizard", "Bulbasaur","Pikachu", "Charizard", "Bulbasaur"] #list

# tuples - ordered, immutable, allow dupes
# indexed
coordinates = (123, 456, 789) #tuples

# set - unordered, mutable, no dupes
atla_set = {"Katara", "Sokka", "Momo","Momo", "Momo"}
# print(atla_set)

pokemon_moves = {"Chancey": "Tackle", "Pikachu":"Thundershock", "Psyduck":"Hypnosis"}

# for pokemon, move in pokemon_moves.items():
#     print(f"{pokemon} uses {move}!")


stack = []

stack.append("Charizard")
stack.append("Bulbasaur")
stack.append("Wheezing")
stack.append("Cubone")

stack.pop()
# print(stack[-1])
#
# print(stack)
# stack.reverse()
# print(stack)


# index = 0
# while index < len(stack):
#     print(stack[index])
#     index += 1



#FIFO - queue
#LIFO - stack


# pokedex_set = set(pokedex)
# print(pokedex_set)


mph = 65

if mph >= 65:
    print("Hey, you're going over the speed limit!")
elif mph >= 30:
    print("Okaaay you're going the speed limit.")
else:
    print("You are going too slow!!!")



# print(pokedex[2])
# print(len(pokedex))