import requests
from jproperties import Properties
import json

#x = requests.get('https://shazam.p.rapidapi.com/songs/list-artist-top-tracks?id=40008598&locale=en-US')


configs = Properties()

with open('../.venv/Scripts/app-config.properties', 'rb') as config_file:
    configs.load(config_file)

print(configs.get("DB_User"))
# PropertyTuple(data='root', meta={})

print(f'Database User: {configs.get("DB_User").data}')
# Database User: root

print(f'Database Password: {configs["DB_PWD"].data}')
# Database Password: root@neon

headers = {"x-rapidapi-host": f"{configs["x-rapidapi-host"].data}",
           "x-rapidapi-key": f"{configs["x-rapidapi-key"].data}"}

url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks?id=40008598&locale=en-US"

response = requests.get(url, headers=headers)

print("Status Code", response.status_code)
#print("JSON Response ", response.json())

url = "https://shazam.p.rapidapi.com/artists/get-details?id=567072&l=en-US"
response = requests.get(url, headers=headers)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

dictionary = dict(response.json())

print(dictionary['data'])



import os
from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env into os.environ

database_url = os.getenv("x-rapidapi-host")
api_key = os.getenv("x-rapidapi-key")