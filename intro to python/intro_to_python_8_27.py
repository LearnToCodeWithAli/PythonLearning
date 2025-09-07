
state = "California" # string
year_established = 1850 # int, whole number
cups_of_sugar = 2.5 # float, floating point number or decimal

# list - ordered, indexable, mutable, allows duplicates
fruits = ["apple", "orange", "strawberries", "blueberries"]
fruits.append("mango")
fruits.append("apple")
# print(fruits)

count_fruit = dict()

for fruit in fruits:
 count_fruit[fruit] = count_fruit.get(fruit, 0) + 1

# print(count_fruit)

# sets - unordered, not indexable, mutable, do not allow duplicates
vegetables = {"caulliflower", "broccoli", "yucca", "carrot", "beet",
              "lettuce"}

# vegetables.add("spinach")
# vegetables.add("lettuce")
# print(vegetables)


# tuple - ordered, indexable, not mutable, allows duplicates
soups = ("Egg Flower Soup", "Ramen", "Beef Stew",
         "Chicken", "Posole", "Caldo de Rez", "Pho")

# dictionaries - key/value pairs
drinks = {"Cancer": "Boba Tea", "Virgo":"Frappe", "Capricorn":"Green Tea",
          "Sagittarius":"Water", "Scorpio":"Mimosa"}

for star_sign, drink in drinks.items():
 print(f"If you are a {star_sign}, then you drink {drink}.")
#
# for each in vegetables:
#  print(f"Harry doesn't like to eat {each}.")

# mad lib program - fill in the blanks



# location = input("Where do you live? ")
# season = input("What's the season? ")
# sentence = f"I went to {location} for the {season}"
#
# print(sentence)

season = "SUMMER"

# if season == "SUMMER":
#  print("It's time to break out the bathing suits")
# elif season == "WINTER":
#  print("It's time to put on a jacket")

# match(season):
#  case "SUMMER":
#   print("It's time to break out the bathing suits!!!")
#  case "WINTER":
#   print("It's time to put on a jacket!")

word = "banana"
# print(word[::-1])

# print(2**3)


# def multiply_value(value, power):
#  if power != 1:
#   power -= 1
#   value = value + value
#   return multiply_value(value, power)
#  return value
#
# print(multiply_value(2,3))

# import threading
# import socket
# import re
# import signal
# import sys
# import time
#
#
#
#
# class Server():
#  def __init__(self, port):
#   self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   self.ip = "localhost"
#
#   self.s.bind((ip,port))
#   self.s.listen()
#   print("Listening on port", port)
#
#   self.client_sockets = []
#   signal.signal(signal.SIGINT, self.signal_handler)
#   signal.signal(signal.SIGTERM, self.signal_handler)
#




server = Server()
threading.Thread(target=server.accepting).start()
threading.Thread(target=server.chatting).start()