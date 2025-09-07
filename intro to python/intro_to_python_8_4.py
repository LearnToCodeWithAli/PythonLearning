# data types, conditional statements, loops, APIs

katara = "My favorite bending is water bending" # string
age = 15 # int
currency = 13.5 # float

greetings = ["hi", "hello", "how are you"] # list - mutable, ordered, duplicates allowed
coordinates = (45,32,12) # tuple - immutable, ordered, duplicates allowed
characters = {"Goku", "Krillin", "Piccolo", "Bulma", "Gohan"} # set - mutable, not ordered, no duplicates

languages = {"python":1991, "java":1995, "javascript":1995, "c++":1983}

# for lengua, year in languages.items():
#     print(f"{lengua} was created in {year}")
#

isHappy = True
isSad = False
#
# if isSad:
#     print("Hi, I'm happy")
# else:
#     print("I'm not happy :(")

# grade = 90
#
# if grade >= 90:
#     print("You got an A!")
# elif grade >= 80:
#     print("You got a B!")
# else:
#     print("You failed the class")

# beginner: learnpython.org, w3Schools,
# more advanced: baeldung, geeksforgeeeks
# tutorialspoint
# paid: udemy, codeacademy (game)

import requests
from jproperties import Properties
import json


configs = Properties()

with open('../.venv/Scripts/app-config.properties', 'rb') as config_file:
    configs.load(config_file)

headers = {"x-rapidapi-host":f"{configs["x-rapidapi-host"].data}",
           "x-rapidapi-key":f"{configs["x-rapidapi-key"].data}"}

# url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks?id=40008598&locale=en-US"
#
# response = requests.get(url, headers=headers)

# print("Status Code", response.status_code)

url = "https://shazam.p.rapidapi.com/artists/get-details?id=567072&l=en-US"

response = requests.get(url, headers=headers)

# print("Status Code", response.status_code)
# print("JSON response ", response.json())

dictionary = dict(response.json())

data = dictionary['data']
#print(data[0]['attributes']['name'])

attributes = data[0].get('attributes')
artist_name = attributes.get('name')
editorial_notes = attributes.get('editorialNotes').get('standard')


artwork = attributes.get('artwork')
artwork_url = artwork.get('url')
artwork_width = artwork.get('width')
artwork_height = artwork.get('height')

print(data[0].get('attributes').get('name'))

print(artwork_url.replace("{w}", f"{artwork_width}").replace("{h}",f"{artwork_height}"))


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 400, 200) # x, y, width, height

        label = QLabel("Hello, PyQt5!", self)
        label.move(150, 80) # position the label

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())




















# 2XX success ex. 200, 201, 204 - success
# 4XX client error ex. 400, 401, 403, 404, 429
# 5XX server error ex. 500, 501, 502, 503, 504 gateway timeout




# curl --request GET
# 	--url 'https://shazam.p.rapidapi.com/artists/get-details?id=567072&l=en-US'
# 	--header 'x-rapidapi-host: shazam.p.rapidapi.com'
# 	--header 'x-rapidapi-key: '

# API - GET, POST, PUT, DELETE














