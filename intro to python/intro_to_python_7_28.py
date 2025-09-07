import random

mochi = "hi hello how are" #string
age = 9 #int
diameter = 3.0 #float

stringray = [1,2,3,4,5] #list
coordinates = (4,5) #tuple
apples = {"red", "green","blue"} #set

oranges = set()
oranges.add("dark orange")
# print(oranges)

isReal = True
isImaginary = False

grades = range(10) #range

ages = {"Katara":15, "Sokka":16, "Aang":112, "Zuko":16}

hashmap = dict()
hashmap["Katara"] = 16

# print("This is Katara's age: " + hashmap["Katara"])
# print("This is Katara's age: " + str(hashmap["Katara"]))
# print(f"This is Katara's age: {hashmap["Katara"]}")
#
# print("Can you use double \"quotes\"?")

# print(True == 1)
# print(True == 2)
# print(False == 0)
# print(False == 1)


#1 data types, string functions, conditionals, loops, methods, classes
#References: W3Schools and Python documentation

def check_gas_level(gas_level):
    if gas_level < 0 or gas_level > 100:
        raise Exception("This gas_level is invalid")
    elif gas_level == 0:
        return "Sorry, you can't go anywhere. Your tank is empty."
    elif gas_level < 30:
        return "Be careful, your tank is low!"
    else:
        return "Where do you want to go"

def fill_tank(gas_level):
    temp = gas_level + random.randint(20,50)

    while temp > 100:
        temp = gas_level + random.randint(20, 50)

    return temp

gas = 10

#print(check_gas_level(gas))
gas = fill_tank(gas)
print(gas)












