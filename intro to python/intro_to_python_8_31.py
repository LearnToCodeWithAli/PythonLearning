tv_show = "atla" # string

number_of_seasons = 4 # int - whole number
number_of_cabbages = 5.5 # float - floating point number

hot = True # bool or boolean
cold = False

# list, tuple, set

#learpython.org
#list - ordered, indexable, mutable, allows duplicates
fruits = ["apricot", "mango", "peach", "apple", "pear"]
#fruits.reverse()
#print(fruits)
#fruits.append
fruits.append("strawberry")
fruits.remove("apricot")
#print(fruits)

# for each in fruits:
#     print(each)

# tuple - ordered, indexable, immutable or not mutable, allows duplicates
vegetables = ("broccoli", "spinach", "cauliflower", "beet")
#print(vegetables[0])

#set - not ordered, not indexable, mutable, no duplicates
dessert = {"brownies", "tiramisu", "pie", "cookies", "cake"}

dessert.add("ice cream")
#print(dessert)

# if "brownies" in dessert:
#     print("There are brownies")

#learnpython.org
# dictionary - key/value pair
drink_preferences = {"Capricorn": "caprisun",
                     "Scorpio": "Rock & Rye",
                     "Libra": "coffee",
                     "Leo": "Long Island",
                     "Aquarius": "Sangria"}

drink_preferences["Leo"] = ["Jamaica", "Coffee"]
drink_preferences["Virgo"] = "Horchata"

for sign, drink in drink_preferences.items():
    if type(drink) is not str and len(drink) > 1:
        drink = drink[0]

    print(f"If you are a {sign}, then you drink {drink}.")

#conditional: if/else, match; loops: for, why


