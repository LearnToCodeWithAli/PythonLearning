
#to add and delete movies

katara = "Hi my name is Katara" #string

basic = "Hello World" #string
age = 12 #int (short for integer)
currency = 12.5 #float, can use decimal places

stingray = [1,2,3,"string","hi",3.4] # list - mutable, ordered, allow duplicates
naga = (123,231,234) # tuple - immutable, ordered, allow duplicates
waffles = {"cat", "dog", "rat", "rat"} #set


isHappy = True
isMad = False

# if isHappy:
#     print("Hooray!")
# else:
#     print("Boooooo")
#
# if isMad:
#     print("Grrrr")
# else:
#     print("Yippee!")

ice_cream = {"chocolate":3, "vanilla":2, "strawberry":5}

# for toes, price in ice_cream.items():
#     print("{toes} costs ${price}")


# print(range(10))
#
# nums = range(10)
#
# for n in nums:
#     print(n, end="")

# data types, conditional statements, for loops
# print(waffles)

# Edit your Path set to the Python directory python.exe

atla = ['Katara', 'Sokka', 'Aang', 'Toph', 'Momo', 'Appa']

for character in atla:
    character = character.upper()
    print(character, end=' ')

# map function
capitalized_characters = list(map(str.upper, atla))
print(capitalized_characters)


#create an object of usernames and loop through it organized by length

usernames = ["happy", "Nujake", "AD343", "Quincy-Jerrod", "Joel", "Arianne"]

user_length = dict()
for name in usernames:
    user_length[len(name)] = name

sorted_list = sorted(user_length.keys())

for each in sorted_list:
    print(user_length[each], end=" ")

print()







