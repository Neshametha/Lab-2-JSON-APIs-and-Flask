import main_functions
import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosty/photos?sol=1000&api_key="

nasa_api_dict = main_functions.read_from_file("nasa_api.json")
my_api_key = nasa_api_dict["nasa_api.json"]

url2 = url + my_api_key

mars_pics = requests.get(url2).json

main_functions.save_to_file(mars_pics, "mars_pics.json")

mars_pics = main_functions.read_from_file("mars_pics.json")

print (mars_pics.keys())

print (type(mars_pics["photos"]))

print (mars_pics["photos"][0].keys())

print (len(mars_pics["photos"]))

print (type(mars_pics["photos"][0]["camera"]))

print (mars_pics["photos"][0]["camera"].keys())

for i in mars_pics["photos"]:
    print(i["camera"]["full_name"])
