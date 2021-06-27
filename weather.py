# importing modules
import requests, json

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/find?"

# City Name
CITY = "Oslo"

# Your API key
API_KEY = "lol"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&units=metric&type=accurate&mode=xml" + "&appid=" + API_KEY

# print url
print(URL)
