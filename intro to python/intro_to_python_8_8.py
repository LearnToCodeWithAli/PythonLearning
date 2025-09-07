

def this_is_a_method():
    print("hi, I'm a method")

johnny_bravo = "Hey Mama" # string

ed = 15 # int
edd = 15.6 # double

characters = [] # list - ordered, mutable (they can change), indexable, allows duplicates
characters.append("Ed")
characters.append("Edd")
characters.append("Eddie")
characters.append("Eddie")

# print(characters)

# this_is_a_method()

atla_characters = set() # set - unordered, mutable (can be changed), not indexable, does not allow duplicates
atla_characters.add("katara")
atla_characters.add("sokka")
atla_characters.add("aang")

countries = {"US","JP","MX"}
countries.add("US")
# print(countries)

temperatures = (200, 360, 400) #tuples - ordered, immutable (they cannot be changed), indexable, allows duplicates
# print(temperatures)

pokemon = {"Machop":"tackle", "Gastly":"smoke bomb", "Bulbasaur":"Vine whip", "Riachu":"Thunderbolt"}

# for poke, move in pokemon.items():
#     print(f"{poke} uses {move} on Wheezing!")

# for index in range(15):
#     print(index, end=" ")
#
# print(4 + 2)

#     conda create --name myenv python=3.9
#     conda activate myenv
#     conda env list

beverages = ["macchiato","chai latte", "kombutcha", "espresso"]

star_sign = "leo"

match (star_sign):
    case "pisces":
        print("You probably drink espresso <3")
    case "capricorn":
        print("I know you drink kombutcha every morning")
    case "virgo":
        print("Sipping on chai latte")




# create an api in python
# tutorial for api in python
# comparison fastapi vs django vs flask
# pros vs cons of fastapi
# fastapi tutorial for beginners





























