
favorite_movie = "Devil Wears Prada" # string
number_of_shoes = 20 # int - whole number
price = 55.99 # float, decimal number - floating point decimal

#list, tuple, set

# list - mutable, indexable, ordered, allows duplicates
best_movies = ["Rocky Horror Picture Show", "Love Simon", "Paris is Burning", "Wong Fu Thanks For Asking", "Rent"]

#
# for each in best_movies:
#     print(each)

# print(best_movies[0])
# best_movies[0] = "But I'm a Cheerleader"
# print(best_movies)

# tuple - immutable, indexable, ordered, allow duplicates
romance_movies = ("The Notebook", "If I Stay", "Princess Diaries",
                  "The Vow", "Me Before You")

# print(romance_movies[0])

# set - mutable, not indexable, not ordered, does not allow duplicates
magazines = {"GQ", "Vogue", "Seventeen"}
# print(magazines)
# magazines.add("National Geographic")
# print(magazines)
# magazines.add("GQ")
# print(magazines[0])

# dictionary - uses key/value pairs
drinks = {"Virgo":"Horchata", "Capricorn": "Black Coffee", "Pisces":"Apple Cider",
          "Aries":"Cranberry Juice","Gemini":"Green Tea"}

# for star_sign, drink in drinks.items():
#     print(f"{star_sign} drinks {drink}")


