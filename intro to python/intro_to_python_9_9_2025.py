
year_of_est = 2007 # int - whole numbers
no_of_customers = 2_000_000_000

subscription_price = 29.99 # float - real number, uses decimal points

company = "Netflix" # string
location = "Santa Monica, CA &%#*$@)!(@*$^&*@#"

is_great_place_for_parents = True #boolean
has_onsite_pool = False

#
# #dynamic typing, implied data types
# #static typing is enforced data types
#
# # tuple - ordered, indexable, not mutable, allow duplicates
# countries = ("Panama", "Kazakhstan", "China", "Mexico", "Russia")
# print(countries[0])
#
# # set - not ordered, not indexable, mutable, do not allow duplicates
# languages = {"English", "German", "French", "Swahili"}
# languages.add("Spanish")
# print(languages)
#
#
# # list - ordered, indexable, mutable, allow duplicates
# oceans = ["Pacific", "Atlantic", "Indian"]
# oceans.append("Arctic")
# print(oceans)
# oceans.remove("Pacific")
# print(oceans)
#
# # dictionary - key/value pairs
# star_signs = {"Virgo":"Matcha", "Capricorn":"Hot Chocolate", "Aquarius":"Milk Tea"}



# for ctry in countries:
#     print(ctry)
#
# for sign, drink in star_signs.items():
#     print(f"{sign} likes to drink {drink}")

# how to do a for loop in c++

# NeetCode

# def get_speed(speed):
#     if speed >= 55:
#         print("You're gonna get a ticket!")
#     elif speed >= 30:
#         print("You're going the speed limit")
#     else:
#         print("You're going too slow, speed up!")
#
# mph = 1
# while mph != 0:
#     mph = int(input("How fast were you going? "))
#     get_speed(mph)



# text = input("type something")
#
# numbers = text.split(",")
# result = []
#
# for number in numbers:
#     if int(number) % 3 == 0 and int(number) % 5 == 0:
#         result.append("FIZZBUZZ")
#     elif int(number) % 3 == 0:
#         result.append("FIZZ")
#     elif int(number) % 5 == 0:
#         result.append("BUZZ")
#     else:
#         result.append(number)
#
#
# print(result, end=", ")



# print(sum(
#     [1,2,3,4,5]))
#


# number of characters in a string

text = "Hello, world!"

count_char = dict()
for x in text:
    count_char[x] = count_char.get(x, 0) + 1

for x in text:
    count_char[x]


# It’s not thinking.. it’s translating from business process flows
# and rules into logical coded strucs


#Fizz Buzz
# For multiples of three, print or say "Fizz".
# For multiples of five, print or say "Buzz".
# For multiples of both three and five, print or say "FizzBuzz".
# For all other numbers, print or say the number itself.

input_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

multiples_of_three = [3,6,9,12,15]
multiples_of_five = [5,10,15]



for element in input_array:

    multiple_of_three = element % 3 == 0
    multiple_of_five = element % 5 == 0

    if multiple_of_three and multiple_of_five:
        print("FizzBuzz" + " ")
    elif multiple_of_three:
        print("Fizz" + " ")
    elif multiple_of_five:
        print("Buzz" + " ")
    elif not multiple_of_three or not multiple_of_five:
        print(str(element) + " ")




















