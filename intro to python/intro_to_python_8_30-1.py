
tv_show = "Garfield and Friends" # string
num_of_seasons = 6 # int - aka whole number
pieces_of_lasagna = 3.5 # float - floating point number

# word = "superficial"
# print(word[3:])
# print(word[0:5])

# list - mutable, ordered, indexable, allows duplicates
fruits = ["apricot", "peach", "apple", "strawberry"]
temp = fruits[0]
fruits[0] = fruits[3]
fruits[3] = temp
fruits.append("apricot")
#print(fruits)
# print(fruits)

# tuple - not mutable, ordered, indexable, allow duplicates
vegetables = ("carrot", "yucca", "broccoli", "celery", "celery")
# print(vegetables)
#vegetables[0] = "hello"
#print(vegetables[2])

# learnpython.org, W3Schools - JavaScript/Python

# set - mutable, not ordered, not indexable, do not allow duplicates
drinks = {"Chai Latte", "Matcha", "Horchata", "Water"}
drinks.add("Agua Fresca de Sandia")

star_signs = ["Virgo", "Capricorn", "Cancer", "Libra", "Taurus"]

#print(list(zip(star_signs, drinks)))

sign_drinks = dict(zip(star_signs, drinks))
#print(sign_drinks)

sign_drinks["Sagitarius"] = "Margarita"

for sign, drink in sign_drinks.items():
    print(f"If you are a {sign}, then you drink {drink}.")



