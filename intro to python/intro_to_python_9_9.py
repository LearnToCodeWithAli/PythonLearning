#


year_of_est = 2007 # int - whole number
no_of_customers = 2_000_000_000

subscription_price = 19.99 # float - floating point number or real number

company = "Netflix" # string
location = "Santa Monica, CA"

is_fun_place_to_work = True
has_onsite_pool = False
#
# # tuple - indexable, ordered, not mutable, allow duplicates
# countries = ("Ethiopia", "Burundi", "Sierra Leone", "Ivory Coast")
# print(countries[0])
#
# # sets - not indexable, not ordered, mutable, do not allow duplicates
# colors = {"blue", "green", "orange","purple"}
# colors.add("black")
# print(colors)
#
# lists - indexable, ordered, mutable, allow duplicates
animals = ["cat", "dog", "bear", "monkey", "tiger"]
animals.append("dolphin")
animals.remove("cat")
# print(animals)
# print(animals[0])

# dictionary - key/value pairs - keys must be unique
star_signs = {"Virgo":"Chai Latte","Taurus":"Orange Juice", "Capricorn":"Coffee"}

# for sign, drink in star_signs.items():
#     print(f"{sign} drinks {drink}")

# for animal in animals:
#     print(animal)





def get_age(age):
    message = ""
    if age >= 65:
        message = "You get a senior discount"
    elif age >= 21:
        message = "You can order an alcoholic drink"
    elif age >= 18:
        message = "You can go to a R-rated movie"
    else:
        message = "You need to be accompanied by a parent"

    print(message)


years = 1
while years != 0:
    years = int(input("How old are you?"))
    get_age(years)