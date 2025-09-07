ice_cream_scoop = "rocky road"  # string - text
num_of_scoops = 3  # int - whole number
cost = 7.99  # float - floating point number

# list, set, tuple

# list- ordered, indexable, mutable, allows duplicates
ice_cream = ["cookies & cream", "mint & chip", "strawberry", "strawberry", "butterscotch"]
ice_cream[1] = "pistachio"
ice_cream.append("cookie dough")
ice_cream.remove("butterscotch")

# print(ice_cream)

# set - not ordered, not indexable, mutable, no duplicates
cars = {"toyota", "honda", "mazda", "ford", "chevrolet", "subaru"}

car = "ford"
# if car in cars:
#     print(f"do not buy another {car}")

cars.add("mitsubishi")
cars.remove("toyota")
# print(cars)

# tuple - ordered, indexable, not mutable, allows duplicates
sports = ("volleyball", "baseball", "futbol", "tennis", "cheer", "ballet")

# print(sports[2])

food = {"bread": "sourdough", "fruit": "melon", "vegetable": "squash",
        "chocolate": "snickers", }

favorite_food = input("what is your favorite food? ")
print(favorite_food)