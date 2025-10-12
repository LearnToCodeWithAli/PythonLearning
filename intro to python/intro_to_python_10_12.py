character = "Ironheart" # string - text
age = 17_000 # int - whole number
cost = 1099.99 # float - floating point number
is_happy = True #boolean

# if is_happy:
#     print("It's a wonderful day!")
# else:
#     print("It's a very sad day.")

# print(f"Riri's age is {age}")
#
# some_text = f"Riri's age is {age}"


flowers = ["tulips", "lilies","roses","orchids"]

# print(flowers[0])
#
# for flower in flowers:
#     print(flower, end=" ")
#
# for i in range(5):
#     print(i)

def check_speed_and_decrement(speed):
    while speed > 0:
        check_speed(speed)
        speed -= 10

    # print("Your current speed is 0")

def check_speed(speed):
        if speed > 50:
            print("You're going too fast, slow down!!")
        elif speed > 35:
            print("You are going the speed limit")
        elif 15 > speed > 0:
            print(f"You're going too slow")
        else:
            print("This is not a valid speed")


# current_speed = input("How fast were you going")
# check_speed_and_decrement(current_speed)

star_sign_drinks = {"leo":"pina colada",
                    "capricorn": "orange juice",
                    "gemini": "fizzy water",
                    "cancers": "long island",
                    "aries": "pepsi",
                    "taurus": "ice water",
                    "aquarius": "tequila",
                    "pisces": "blood of enemies"}

# for sign, drink in star_sign_drinks.items():
#     print(f"{sign} likes to drink {drink}")

# list - ordered, indexable, mutable, allow duplicates
fruits = ["apple", "mango", "grape","pineapple"]

# tuple - ordered, indexable, not mutable, allows duplicates
vegetables = ("carrot", "lettuce", "broccoli")

# mutable - it can be changed
# change individual elements,
# add to the list
# remove from the list

#immutable - static, constant, cannot be changed

# print(vegetables[0])
#
# fruits[0] = "orange"
# print(fruits)
# fruits.append("pear")
# print(fruits)
# fruits.remove("grape")
# print(fruits)


# stack - LIFO - last in first out
# queue - FIFO - first in first out

stack = ["orange", "apple", "banana"]

# adding to the stack
stack.append("raspberry")
stack.append("blueberry")
print(stack.pop())
stack.append("apricot")
del stack[len(stack)-1]

print(stack)























