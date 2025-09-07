


# x = 5
# y = 6
#
# print(y < x)
#
# name = "Mikey"
#
# print(name)
#
# for each in name:
#     print(each + " ", end="")
#
# print()
#
# for i in range(len(name)):
#     print(name[i] + "-", end="")
#
# print()
# print(len(name))
# print(range(5))
#
# for i in range(5):
#     print(i, end="")


x = True
y = False

#print(x)

fish_1 = 10
fish_2 = 10

# if fish_1 > fish_2:
#     print("fish 1 is bigger")
# elif fish_2 > fish_1:
#     print("fish 2 is bigger")
# else:
#     print("They're the same size, duh")


fish = dict()

fish["Larry"] = 5
fish["Moose"] = 2

# if fish["Larry"] > fish["Moose"]:
#     print("Larry is bigger than Moose")
# elif fish["Moose"] > fish["Larry"]:
#     print("Moose is bigger than Larry")
# else:
#     print("Larry and Moose are the same size")
#
# print(fish)

koi = {"Katara": 11,
       "Sokka": 12,
       "Aang": 8,
       "Zuko": 16}

print(koi["Katara"])

for fish_name, size in koi.items():
    message = f"My koi fish named {fish_name} is {size} inches long"
    print(message)


class Koi:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color

koi1 = Koi("Katara",11,"blue")
koi2 = Koi("Sokka",12,"blue")
koi3 = Koi("Aang",8,"orange and yellow")
koi4 = Koi("Zuko",16,"red")

if koi2.size > koi1.size:
    print(koi2.name + " is bigger than " + koi1.name)
