
# data types
my_favorite_drink = "earl gray tea with milk" # string
issue_no = 32 # int - whole number
cost = 2.99 # float - floating point number

is_tea_hot = True # boolean
is_tea_cold = False

if is_tea_hot and not is_tea_cold:
    print("drink the tea")

# list - ordered, indexable, mutable, allow duplicates
fruits = ["orange", "apple", "pear", "banana"]
# print(fruits[0])
# fruits.append("grapefruit")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
#
# print(fruits.pop())
# print(fruits)

# tuples - ordered, indexable, immutable, allow duplicates
vegetables = ("carrot", "zucchini","potato","beet")
print(vegetables[0])

almost_a_list = "carrot,zucchini,potato,beet"

print(almost_a_list.split(","))


# set - unordered, not indexable, mutable, do not allow duplicates
drinks = {"matcha","dr pepper","chai", "pepsi","smoothie"}

my_favorites = {"matcha", "chai","horchata"}

print(drinks.intersection(my_favorites))



#1 - how to get started on a personal project