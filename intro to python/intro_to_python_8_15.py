# Refs: W3Schools and Python docs, GeeksForGeeks, Baeldung, TutorialsPoint, LearnPython.org

katara = "I am a waterbender" # string
appa = 4 # int - whole number
momo_age = 2.5 # float

# list - mutable, indexable, ordered, allow duplicates
atla_characters = ["katara", "aang", "sokka", "toph"]

#print(atla_characters[len(atla_characters)-1])
atla_characters.append("zuko")
#print(atla_characters)
atla_characters[0] = "azula"
#print(atla_characters)
atla_characters.append("aang")
#print(atla_characters)

# print("zuko" == "Zuko")
# print("zuko" == "zuko")

# tuple - immutable, indexable, ordered, allow duplicates
locations = ("Southern Water Tribe",
             "Northern Water Tribe",
             "Earth Kingdom",
             "Fire Kingdom",
             "Air Temples")

# print(locations)
#locations.append("hat")

# print(type(locations))
# print(type(atla_characters))

dice = [1,2,3,4,5,6]

# set - mutable, not ordered, not indexable, do not allow dupes
companions = {"appa", "momo", "naga", "pabu"}
#print(companions)
companions.add("flopsie")
#print(companions)
companions.add("appa")
#print(companions)


# dictionaries - key:value pairs, keys must be unique
pokemon = {"Bulbasaur":"Razor Leaf", "Squirtle":"Water Gun", "Pikachu":"Thunderbolt"}

# for monster, moves in pokemon.items():
#     print(f"{monster} uses {moves} on Wheezing")
#
# for element in pokemon.items():
#     print(element)

list_of_numbers = [1,2,3,4,5,6,7]

# print(list_of_numbers)
#
# for each in list_of_numbers:
#     print(each)

# for each in range(10):
#     print(each)



import requests
import bs4
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 OPR/120.0.0.0"
}
request = requests.get("https://time.is")
print(request.text)
soup = bs4.BeautifulSoup(request.text,"html.parser")
print(soup.find("div",id="clock0_bg").text)









