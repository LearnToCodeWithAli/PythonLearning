# learnpython.org, w3schools, python documentation
# baeldung, tutorialspoints

andrew_garfield = 32 # int
money = 4.5 # float
katara = "I am waterbender" #string

# allow duplicates, ordered, indexable
# mutable, can be changed
atla_characters = ["Sokka",
                   "Katara",
                   "Aang",
                   "Toph"] # list

# allow duplicates, ordered, indexable
# immutable - cannot be changed
coordinates = (4,3,1) # tuple

# does not allow duplicates, not ordered
# mutable, not indexable
atla = {"Momo", "Appa", "Naga", "Naga"}

# print(atla)
# atla.add("Naga")
# print(atla)

atla = set()
atla.add("Naga")
atla.add("Aang")
atla.add("naga")
# print(atla)

# characters = []
# characters.append("Linux")
# print(characters)

pokemon = {"Pikachu":"Thundershock",
           "Bulbasaur":"Razor Leaf",
           "Psyduck": "Confusion"}

# for poke, move in pokemon.items():
#     print(f"{poke} uses {move} on Mr. Mime")
#
# for index in range(10):
#     print(index, end=" ")
#
#
# cup_of_tea = 100
#
#
# if cup_of_tea < 100:
#     print("Fill the cup")

# import threading
#
# def first_function(num):
#     while int(num) > 0:
#         num -= 1
#         print(num)
#
# def second_function(letter):
#     while ord(letter) < 132:
#         print(letter)
#         letter = chr(ord(letter) + 1)
#
# t1 = threading.Thread(target=first_function, args=(100,))
# t2 = threading.Thread(target=second_function, args="A")
#
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


katara = "I hate Sokka" # string
sokka_age = 16 #int = whole number
money = 2_000_000.55 #float

greetings = [] #list
greetings.append("hello")
greetings.append("how are you")

temp = (123,1234,212) #tuple

spiderverse = {"spider-gwen", "spider-man","spider-punk"} #set
spiderverse.add("spider-punk")

languages = {"python":1991,"javascript":1995,"java":1995}

# for language,year in languages.items():
#     print(f"{language} was created in {year}")

# for i in range(14):
#     print(i, end=" ")

grade = 80
message = ""

if grade >= 90:
    message = "You get an A!"
elif grade >= 80:
    message = "You got a B!"
elif grade >= 70:
    message = "You got a C!"
else:
    message = "You should really study"

import random

season = random.randint(1,3)

# match season:
#     case 1:
#         print("Book of Water")
#     case 2:
#         print("Book of Earth")
#     case 3:
#         print("Book of Fire")



# print(message)


# print(greetings)

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
host_url = os.getenv("x-rapidapi-host")
api_key = os.getenv("x-rapidapi-key")

url = "https://shazam.p.rapidapi.com/artists/get-details?id=567072&l=en-US"

headers = {"x-rapidapi-key":api_key,
           "x-rapidapi-host": host_url}

response = requests.get(url,headers=headers)

print("Status Code ", response.status_code)
# print("JSON Response ", str(response.json()))

dictionary = response.json()

data = dictionary['data'][0]['artwork']


