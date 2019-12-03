'''Natalie Whitehead'''

import json
import requests

def save_to_file(data,file_name):
    with open(file_name, "w") as write_file:
        json.dump(data, write_file, indent=4)
        print("The file {0} was successfully created.".format(file_name))

def read_from_file(file_name):
    with open(file_name, "r") as read_file:
        file=json.load(read_file)
        print("You successfully read from {0}.".format(file_name))
        return file

my_aqi_api_key = read_from_file(("api_key.json"))
my_aqi_api_key = my_aqi_api_key["aqi_api_key"]

url = "http://api.airvisual.com/v2/nearest_city?key="
url_aqi = url + my_aqi_api_key

aqi = requests.get(url_aqi).json()
save_to_file(aqi, "aqi.json")

air_quality_index = read_from_file("aqi.json")

latitude = air_quality_index["data"]["location"]["coordinates"][0]
longitude = air_quality_index["data"]["location"]["coordinates"][1]
print("latitude: {} \nlongitude: {}".format(latitude, longitude))