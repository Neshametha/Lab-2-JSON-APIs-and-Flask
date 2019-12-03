import json
import main_functions
import requests

my_nasa_api = main_functions.read_from_file(("nasa_api.json"))
my_nasa_api = my_nasa_api["nasa_api"]

url = "https://api.nasa.gov/planetary/apod?api_key="
url2 = url + my_nasa_api

# apod = requests.get(url2).json()
# main_functions.save_to_file(apod,"apod.json")

apod = main_functions.read_from_file("apod.json")

print (type(apod))
print (apod.keys())
print (apod["url"])
print (apod["explanation"])
